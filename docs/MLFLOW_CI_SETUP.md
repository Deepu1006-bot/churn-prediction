# MLflow and GitHub Actions CI Setup

## 1. Aim
To configure MLflow experiment tracking and integrate the churn prediction MLOps pipeline with GitHub Actions.

## 2. MLflow Configuration
MLflow settings are maintained in `config.yaml`.

- Tracking URI: `sqlite:///mlflow.db`
- Experiment name: `Telco_Churn_Prediction`
- Registered model name: `Telco_Churn_Production_Model`
- Decision metric: `f1_score`

## 3. Local Execution
Activate the project virtual environment and run the pipeline from the project root:

`python src/mlops_pipeline/churn_prediction_pipeline.py`

The pipeline trains and evaluates the model, logs experiment information, registers the model, checks the quality gate, and performs inference.

## 4. GitHub Actions Configuration
The CI workflow is stored in `.github/workflows/lab8_ci.yml`.

The Lab 9 workflow is stored in `.github/workflows/lab9_failure_tests.yml`.

Both workflows install dependencies from `requirements.txt`. The workflow environment can obtain `MLFLOW_TRACKING_URI` from GitHub Actions repository secrets.

## 5. Repository Secret
If a custom tracking server is being used, configure the repository secret named `MLFLOW_TRACKING_URI` with its appropriate tracking URI.

For local SQLite tracking, ensure the workflow and pipeline configuration are consistent with the intended storage setup.

## 6. Generated Evidence
The workflows are configured to upload available reports, logs, model files, and other generated outputs as artifacts.

## 7. Execution Status
Local pipeline execution has been verified successfully. GitHub Actions execution must be checked separately in the repository's Actions tab.

## 8. Conclusion
MLflow provides experiment tracking and model registry functionality, while GitHub Actions automates pipeline execution. Successful integration should be confirmed using the actual workflow run and its artifacts.
