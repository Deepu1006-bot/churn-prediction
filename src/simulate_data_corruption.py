
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "raw" / "churn.csv"
OUTPUT_PATH = PROJECT_ROOT / "data" / "raw" / "churn_corrupted.csv"


def simulate_data_corruption():
    """Create a corrupted copy without modifying the original dataset."""

    if not INPUT_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {INPUT_PATH}"
        )

    df = pd.read_csv(INPUT_PATH)

    if "MonthlyCharges" not in df.columns:
        raise ValueError(
            "Required column 'MonthlyCharges' is missing."
        )

    # Inject an invalid numeric value into the copied dataset.
    df["MonthlyCharges"] = df["MonthlyCharges"].astype(object)
    df.loc[0, "MonthlyCharges"] = "INVALID_NUMBER"

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print("[SUCCESS] Corrupted dataset created.")
    print(f"[INFO] Original dataset preserved: {INPUT_PATH}")
    print(f"[INFO] Corrupted copy saved to: {OUTPUT_PATH}")
    print(f"[INFO] Dataset shape: {df.shape}")
    print("[INFO] Injected corruption: MonthlyCharges = INVALID_NUMBER")


if __name__ == "__main__":
    simulate_data_corruption()
