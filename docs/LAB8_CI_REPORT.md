# LAB 8 – Continuous Integration for the MLOps Pipeline

## 1. Aim
To configure a GitHub Actions workflow for automatically executing and validating the churn prediction MLOps pipeline.

## 2. Workflow Configuration
The workflow is defined in `.github/workflows/lab8_ci.yml`.

It is configured to run on:
- Pushes to `main` or `master` when specified project files change.
- Pull requests when specified project files change.
- Manual execution using `workflow_dispatch`.

## 3. Workflow Steps
1. Check out the GitHub repository.
2. Set up Python 3.11.
3. Install dependencies from `requirements.txt`.
4. Execute `src/mlops_pipeline/churn_prediction_pipeline.py`.
5. Upload generated artifacts, reports, logs, outputs, models, and MLflow files when available.

## 4. MLflow Configuration
The workflow reads `MLFLOW_TRACKING_URI` from GitHub Actions repository secrets. The project configuration provides a local SQLite tracking URI as a fallback when the environment variable is unset.

## 5. Expected Evidence
The workflow is intended to generate CI execution evidence and upload available outputs as a GitHub Actions artifact.

## 6. Execution Status
The local MLOps pipeline completed successfully. The GitHub Actions CI workflow result has not yet been verified; therefore, a successful CI run is not claimed in this report.

## 7. Conclusion
The GitHub Actions workflow is configured to automate pipeline execution and collect outputs. Its actual CI status must be confirmed from the workflow run in the GitHub Actions tab.
