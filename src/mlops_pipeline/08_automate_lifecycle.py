
import os
import sys
import json
from pathlib import Path
from datetime import datetime

import mlflow
import yaml
from mlflow.tracking import MlflowClient


def configure_mlflow(config):
    tracking_uri = (
        os.getenv("MLFLOW_TRACKING_URI")
        or config["mlflow"].get("tracking_uri")
    )
    if tracking_uri:
        mlflow.set_tracking_uri(tracking_uri)


def save_lifecycle_report(status, model_name, message, **details):
    report_dir = Path("reports")
    report_dir.mkdir(parents=True, exist_ok=True)

    report = {
        "status": status,
        "model_name": model_name,
        "message": message,
        "timestamp": datetime.now().isoformat(),
        **details,
    }

    report_path = report_dir / "lifecycle_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    print(f"[INFO] Lifecycle report saved to {report_path}")


def automate_model_lifecycle():
    print("[INFO] Starting Automated Model Lifecycle Manager...")

    model_name = "unknown"

    try:
        with open("config.yaml", "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        configure_mlflow(config)

        client = MlflowClient()
        model_name = config["registry"]["model_name"]
        metric_to_optimize = config["registry"]["decision_metric"]

        # 1. Move newly registered models to Staging.
        all_versions = client.search_model_versions(
            f"name='{model_name}'"
        )
        new_models = [
            mv for mv in all_versions
            if mv.current_stage == "None"
        ]

        for mv in new_models:
            client.transition_model_version_stage(
                name=model_name,
                version=mv.version,
                stage="Staging",
                archive_existing_versions=False,
            )
            print(f"[INFO] Version {mv.version} moved to Staging.")

        # 2. Find models in Staging.
        all_versions = client.search_model_versions(
            f"name='{model_name}'"
        )
        models_staging = [
            mv for mv in all_versions
            if mv.current_stage == "Staging"
        ]

        if not models_staging:
            print("[INFO] No models in Staging. Nothing to promote.")

            production_models = [
                mv for mv in all_versions
                if mv.current_stage == "Production"
            ]

            save_lifecycle_report(
                "success",
                model_name,
                "No models in Staging. No promotion required.",
                production_version=(
                    production_models[0].version
                    if production_models else None
                ),
                promoted=False,
            )
            return True

        # 3. Select the best Staging model.
        best_model = None
        best_score = float("-inf")

        for mv in models_staging:
            run = client.get_run(mv.run_id)
            score = run.data.metrics.get(metric_to_optimize, 0.0)

            print(
                f"[INFO] Staging Version {mv.version} | "
                f"{metric_to_optimize}={score:.4f}"
            )

            if score > best_score:
                best_score = score
                best_model = mv

        # 4. Find the current Production model.
        production_models = [
            mv for mv in all_versions
            if mv.current_stage == "Production"
        ]
        production_model = (
            production_models[0] if production_models else None
        )

        if production_model is None:
            move_to_production = True
            production_score = None
            print(
                "[INFO] No Production model exists. "
                "Staging model will become Production."
            )
        else:
            production_run = client.get_run(production_model.run_id)
            production_score = production_run.data.metrics.get(
                metric_to_optimize, 0.0
            )

            print(
                f"[INFO] Production Version {production_model.version} | "
                f"{metric_to_optimize}={production_score:.4f}"
            )

            move_to_production = best_score > production_score

            if move_to_production:
                print("[SUCCESS] Staging model is better than Production.")
            else:
                print("[INFO] Production model remains unchanged.")

        # 5. Promote the better model or archive it.
        promoted = False

        if move_to_production:
            client.transition_model_version_stage(
                name=model_name,
                version=best_model.version,
                stage="Production",
                archive_existing_versions=False,
            )

            if production_model:
                client.transition_model_version_stage(
                    name=model_name,
                    version=production_model.version,
                    stage="Archived",
                    archive_existing_versions=False,
                )

            promoted = True
            print(
                f"[SUCCESS] Version {best_model.version} "
                "is now Production."
            )

        else:
            client.transition_model_version_stage(
                name=model_name,
                version=best_model.version,
                stage="Archived",
                archive_existing_versions=False,
            )
            print(
                f"[INFO] Version {best_model.version} archived "
                "because it did not improve."
            )

        # 6. Archive any other models left in Staging.
        final_versions = client.search_model_versions(
            f"name='{model_name}'"
        )

        for mv in final_versions:
            if mv.current_stage == "Staging":
                client.transition_model_version_stage(
                    name=model_name,
                    version=mv.version,
                    stage="Archived",
                    archive_existing_versions=False,
                )

        print("[SUCCESS] Automated Model Lifecycle execution complete!")

        save_lifecycle_report(
            "success",
            model_name,
            "Model lifecycle completed successfully.",
            decision_metric=metric_to_optimize,
            best_staging_version=str(best_model.version),
            best_staging_score=best_score,
            previous_production_version=(
                str(production_model.version)
                if production_model else None
            ),
            previous_production_score=production_score,
            promoted=promoted,
            final_production_version=(
                str(best_model.version)
                if promoted
                else (
                    str(production_model.version)
                    if production_model else None
                )
            ),
        )

        return True

    except Exception as exc:
        print(f"[ERROR] Failed to automate model lifecycle: {exc}")

        try:
            save_lifecycle_report(
                "failed",
                model_name,
                str(exc),
            )
        except Exception as report_error:
            print(
                f"[ERROR] Could not save lifecycle report: "
                f"{report_error}"
            )

        return False


if __name__ == "__main__":
    passed = automate_model_lifecycle()
    sys.exit(0 if passed else 1)
