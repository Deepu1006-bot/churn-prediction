# LAB 9 – Failure Handling and Recovery in MLOps

## 1. Aim
To study failure handling and recovery in an MLOps pipeline by introducing controlled failures and checking whether the pipeline handles them appropriately.

## 2. Failure Testing Script
The failure-testing script is located at:

`src/mlops_pipeline/10_failure_injection.py`

The script is intended to simulate selected failure scenarios and record the corresponding results.

## 3. Failure Handling Workflow
The Lab 9 workflow is defined in:

`.github/workflows/lab9_failure_tests.yml`

It is configured for manual execution using GitHub Actions. The workflow installs project dependencies, runs the normal pipeline, executes the failure-testing script, and uploads available evidence.

## 4. Evidence and Reports
The workflow is configured to collect available files from:
- `reports/`
- `artifacts/`
- `logs/`
- `outputs/`

The actual failure scenarios, recovery behavior, and test results must be documented from the generated report and execution logs.

## 5. Execution Status
The normal local MLOps pipeline has completed successfully. The Lab 9 failure-injection test results have not yet been verified, so no claim is made that all failure tests passed.

## 6. Conclusion
Failure injection helps evaluate the robustness of an MLOps workflow. The final conclusion should be updated after running the failure-testing script and examining its actual results.
