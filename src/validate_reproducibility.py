import os
import json
import hashlib
import numpy as np


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")


def file_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def validate_file(filepath):
    if os.path.exists(filepath):
        size = os.path.getsize(filepath)
        file_hash_value = file_hash(filepath)

        print(f"[OK] {os.path.basename(filepath)}")
        print(f"     Size : {size} bytes")
        print(f"     SHA256: {file_hash_value}")

        return True

    print(f"[ERROR] Missing file: {filepath}")
    return False


def main():
    print("\n--- Reproducibility Validation ---")

    required_files = [
        "X_train_final.npy",
        "X_test_final.npy",
        "y_train.npy",
        "y_test.npy",
        "dataset_metadata.json"
    ]

    all_valid = True

    for filename in required_files:
        filepath = os.path.join(PROCESSED_DIR, filename)

        if not validate_file(filepath):
            all_valid = False

    print("\n--- Dataset Shape Validation ---")

    try:
        X_train = np.load(
            os.path.join(PROCESSED_DIR, "X_train_final.npy")
        )
        X_test = np.load(
            os.path.join(PROCESSED_DIR, "X_test_final.npy")
        )
        y_train = np.load(
            os.path.join(PROCESSED_DIR, "y_train.npy")
        )
        y_test = np.load(
            os.path.join(PROCESSED_DIR, "y_test.npy")
        )

        print(f"X_train shape: {X_train.shape}")
        print(f"X_test shape : {X_test.shape}")
        print(f"y_train shape: {y_train.shape}")
        print(f"y_test shape : {y_test.shape}")

        if X_train.shape[0] == y_train.shape[0]:
            print("[OK] Training feature/label counts match.")
        else:
            print("[ERROR] Training feature/label counts do not match.")
            all_valid = False

        if X_test.shape[0] == y_test.shape[0]:
            print("[OK] Testing feature/label counts match.")
        else:
            print("[ERROR] Testing feature/label counts do not match.")
            all_valid = False

    except Exception as e:
        print(f"[ERROR] Dataset validation failed: {e}")
        all_valid = False

    print("\n--- Metadata Validation ---")

    metadata_path = os.path.join(
        PROCESSED_DIR,
        "dataset_metadata.json"
    )

    try:
        with open(metadata_path, "r") as f:
            metadata = json.load(f)

        print("[OK] dataset_metadata.json is valid JSON.")
        print(f"Metadata keys: {list(metadata.keys())}")

    except Exception as e:
        print(f"[ERROR] Metadata validation failed: {e}")
        all_valid = False

    print("\n--------------------------------")

    if all_valid:
        print("[SUCCESS] Reproducibility validation passed!")
        return 0

    print("[ERROR] Reproducibility validation failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())