# Telco Customer Churn Prediction — MLOps Project

An end-to-end Machine Learning Operations (MLOps) project that demonstrates how a customer churn prediction model can be prepared, trained, evaluated, versioned, served, monitored, and tested through automated workflows.

**GitHub repository:** [Deepu1006-bot/churn-prediction](https://github.com/Deepu1006-bot/churn-prediction)  
**Primary branch:** `main`  
**Project:** MLOps Labs 1–13

---

## Project Overview

Customer churn prediction estimates whether a customer is likely to stop using a service. This project uses a Telco Customer Churn dataset and develops an MLOps workflow around the model lifecycle, from dataset preparation to API serving, monitoring, and deployment experiments.

The work is organized into 13 experiments covering data preparation, baseline modelling, Git version control, MLflow tracking, data validation, model registry, pipeline engineering, CI automation, failure handling, FastAPI serving, Docker/Kubernetes deployment, drift monitoring, and end-to-end integration.

A key lifecycle principle is that a newly trained model is not automatically promoted to Production. Candidate models are evaluated against configured quality criteria and lifecycle decisions before deployment.

## Objectives

- Prepare and validate customer churn data.
- Build and evaluate baseline classification models.
- Maintain reproducible code and dataset changes with Git.
- Track experiments, metrics, parameters, and artifacts using MLflow.
- Validate input schemas and preprocessing outputs.
- Manage model versions and lifecycle stages.
- Build modular and repeatable ML pipelines.
- Automate selected checks with GitHub Actions.
- Test pipeline failure handling and recovery.
- Serve predictions through a FastAPI application.
- Package the API and model using Docker.
- Explore deployment and service management with Kubernetes.
- Monitor API behaviour and data, prediction, and concept drift.
- Document and test the integrated MLOps workflow.

## MLOps Experiments

| Experiment | Topic | Main work |
|---|---|---|
| 1 | ML project initialization and dataset preparation | Dataset inspection, missing-value and datatype analysis, preprocessing, reproducible splitting, repository organization, and documentation |
| 2 | Baseline model development and evaluation | Logistic Regression, Decision Tree, and Random Forest experiments; evaluation metrics; model serialization |
| 3 | Git-based version control and collaboration | Repository management, commits, branches, merges, rollback/revert, and conflict resolution |
| 4 | Experiment tracking and reproducibility | MLflow parameters, metrics, artifacts, run comparison, and experiment lineage |
| 5 | Data validation and reproducible pipelines | Schema checks, datatype and category validation, reusable preprocessing, and output validation |
| 6 | Model registry and version management | Model registration, version metadata, staging/production lifecycle concepts, comparison, and traceability |
| 7 | ML pipeline engineering | Modular preprocessing, training, validation, evaluation, and inference stages |
| 8 | Pipeline automation and CI | Trigger-based automation and GitHub Actions workflow checks |
| 9 | Pipeline failure handling and recovery | Simulated data/schema/artifact failures, validation, error handling, and recovery checks |
| 10 | FastAPI model serving | Health, metadata, prediction, and batch-prediction API functionality with request validation |
| 11 | Containerization and deployment | Docker image/container testing and Kubernetes deployment/service exercises |
| 12 | Monitoring, drift detection, and retraining | API monitoring, data/prediction/concept drift analysis, model comparison, and retraining workflow exercises |
| 13 | End-to-end MLOps mini project | Integration of model serving and containerized API testing, with Kubernetes exposure and project documentation |

## Architecture and Workflow

The project contains a model lifecycle pipeline and separate serving/monitoring components.

### Model lifecycle pipeline

```text
Dataset loading
      |
Raw data validation
      |
Preprocessing
      |
Processed-output validation
      |
Model training and MLflow tracking/registration
      |
Model evaluation
      |
Quality gate
      |
Lifecycle comparison and model-version decision
      |
Deployment preparation (when applicable)
      |
Inference
```

### API serving and container workflow

```text
Client request
     |
FastAPI application
     |
Request/schema validation
     |
Model and preprocessor loading
     |
Prediction
     |
Structured response and inference logging
```

The API includes health and metadata checks, prediction endpoints, and batch prediction functionality. The Docker workflow builds an image, starts the API container, checks health, verifies that the model and preprocessor loaded, and sends a test prediction.

### Monitoring workflow

Monitoring components generate and combine reports for data drift, prediction drift, and concept drift. Performance and API monitoring scripts record operational metrics. Retraining and registry-update scripts are separate operations; they should be run deliberately because they can change datasets, models, or registry state.

## Dataset

The primary dataset is stored at:

```text
data/raw/churn.csv
```

The project also uses processed datasets and generated monitoring data under `data/processed/` and `data/monitoring/` (where present).

Important dataset fields include the customer identifier, churn target, customer tenure, monthly and total charges, contract type, internet service, and payment method.

For a new-data ingestion exercise, use the expected schema and follow the validation and lineage rules implemented by the project scripts. Do not replace the primary dataset with an arbitrary CSV.

## Model Evaluation and Monitoring

The project evaluates classification models using standard metrics, including:

- Accuracy
- Precision
- Recall
- F1 score
- ROC-AUC
- Confusion matrix

The monitoring exercises include data-drift, prediction-drift, and concept-drift reports. A retrained candidate should be evaluated and compared with the existing model before any promotion or production deployment decision.

**Example recorded monitoring results from the Lab 12 exercise:**

- Data drift was detected in `MonthlyCharges` and `TotalCharges` (2 of 6 monitored features).
- Prediction and probability distributions showed drift.
- The baseline model's recall was `0.6791`, below the configured `0.70` quality threshold.
- The retrained V2 candidate achieved recall `0.7112` and F1 `0.6230` in that exercise.
- The V2 candidate was registered in Staging; the existing V1 model remained in Production and V2 was not promoted.

These are recorded experiment results, not guaranteed results for every future run.

## Technology Stack

| Area | Tools |
|---|---|
| Programming | Python |
| Data processing | pandas, NumPy |
| Machine learning | scikit-learn, Random Forest and other baseline classifiers |
| Data validation | Pandera and project validation utilities |
| Experiment tracking and registry | MLflow |
| API | FastAPI, Uvicorn, Pydantic |
| Model persistence | Joblib / pickle artifacts |
| Containerization | Docker |
| Orchestration exercises | Kubernetes, kubectl |
| Version control | Git and GitHub |
| CI automation | GitHub Actions |
| Configuration and reports | YAML, JSON, CSV |

## Repository Structure

The repository is organized around these main components:

```text
churn-prediction/
├── .github/
│   └── workflows/          # GitHub Actions workflows
├── api/                    # FastAPI application, schemas, model loading
├── data/
│   ├── raw/                # Source churn datasets
│   ├── processed/          # Processed datasets and splits
│   └── monitoring/         # Monitoring/drift datasets (where present)
├── deployment/             # Model, preprocessor, metadata, deployment code
├── docs/                   # Lab reports and project documentation
├── k8s/                    # Kubernetes deployment and service manifests
├── models/                 # Trained model artifacts
├── notebooks/              # Notebook-based experiments
├── pipelines/              # Lab-specific pipeline entry points
├── reports/                # Evaluation, quality, and lifecycle reports
├── src/
│   └── mlops_pipeline/     # Modular MLOps pipeline scripts
├── tests/                  # API and integration tests
├── Dockerfile
├── config.yaml
├── requirements.txt
└── requirements-api.txt
```

Generated files and local runtime data may not all be committed to Git. Refer to `.gitignore` before adding datasets, model artifacts, logs, virtual environments, or MLflow tracking files.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Deepu1006-bot/churn-prediction.git
cd churn-prediction
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

For the complete development environment:

```bash
python -m pip install -r requirements.txt
```

For API-only execution:

```bash
python -m pip install -r requirements-api.txt
```

Use the dependency file appropriate to the task. Docker builds for the API use `requirements-api.txt`.

## Running the API Locally

Start the FastAPI application from the repository root:

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

Useful endpoints:

| Endpoint | Purpose |
|---|---|
| `GET /health` | Check API health |
| `GET /metadata` | Check model/preprocessor loading metadata |
| `POST /predict` | Predict churn for one customer |
| `POST /predict/batch` | Run batch predictions |

Interactive API documentation is available at:

```text
http://localhost:8000/docs
```

The API requires the model and preprocessor artifacts expected by the model loader to be available in the deployment directory.

## Docker

Build the API image:

```bash
docker build -t churn-prediction-api:lab13 .
```

Run the container:

```bash
docker run -d --name churn-api-lab13 -p 8000:8000 churn-prediction-api:lab13
```

Check the health endpoint:

```bash
curl http://localhost:8000/health
```

View logs and stop/remove the container:

```bash
docker logs churn-api-lab13
docker rm -f churn-api-lab13
```

## Kubernetes

The repository includes Kubernetes deployment and service manifests under `k8s/`. Kubernetes exercises were performed against the local Docker Desktop Kubernetes cluster.

Typical commands (use only when the local cluster is running):

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get deployments
kubectl get pods
kubectl get services
```

If direct NodePort access is unavailable in the local environment, use port forwarding to test the service:

```bash
kubectl port-forward service/churn-prediction-service 8081:8000
```

Then open `http://localhost:8081/health`.

The GitHub-hosted CI workflow does not access the developer's local Kubernetes cluster; Kubernetes verification is a separate local exercise.

## GitHub Actions

The repository contains separate workflows for selected lab checks. The latest verified runs on the `main` branch are:

| Workflow | Commit | Result |
|---|---|---|
| Lab 12 – Monitoring and Drift Analysis | `ab42280` | Passed |
| Lab 13 – End-to-End Docker API Testing | `52b371f` | Passed |

The Lab 12 workflow runs the combined drift-analysis report step and verifies that the expected report is generated. It does not perform the full retraining and model-promotion lifecycle.

The Lab 13 workflow builds the Docker image, starts the FastAPI container, checks the health endpoint, verifies model and preprocessor loading, sends a sample prediction request, and cleans up the container.

To view workflow runs, open the repository's **Actions** tab:

[GitHub Actions – churn-prediction](https://github.com/Deepu1006-bot/churn-prediction/actions)

## Important Reports and Documentation

Useful project documentation and reports include:

- `docs/ARCHITECTURE.md` — system architecture.
- `docs/LAB13_END_TO_END.md` — end-to-end project notes.
- `docs/LAB7_PIPELINE.md` — pipeline engineering documentation.
- `docs/LAB8_CI_REPORT.md` — CI workflow documentation.
- `docs/LAB9_FAILURE_HANDLING_REPORT.md` — failure-handling documentation.
- `docs/lab11_containerization_report.md` — containerization report.
- `docs/lab11_deployment_debugging_report.md` — deployment debugging notes.
- `reports/` and `artifacts/` — generated evaluation, validation, monitoring, and performance outputs (where present).

## Notes and Limitations

- The GitHub Actions Lab 13 workflow validates Docker image build and FastAPI container behaviour. It does not deploy to or test the developer's local Kubernetes cluster.
- The Lab 12 CI workflow validates the combined drift-analysis report. It does not automatically prove that retraining, registry promotion, and production deployment all completed.
- The V2 model from the recorded Lab 12 exercise was in Staging; V1 remained in Production. Do not describe V2 as deployed.
- Scripts that ingest data, retrain models, or update the MLflow registry can modify project state. Review their purpose before running them.
- Results and generated artifacts can change when the dataset, configuration, dependencies, or random seeds change.
- Do not commit `.venv/`, secrets, credentials, large temporary files, or unintended local runtime artifacts.

## Conclusion

This project demonstrates the main stages of an MLOps lifecycle through 13 lab experiments: data preparation, model development, experiment tracking, validation, version management, pipeline automation, failure handling, API serving, containerization, monitoring, and end-to-end testing. The Lab 12 monitoring workflow and Lab 13 Docker/FastAPI workflow have both passed on GitHub Actions, while Kubernetes deployment was exercised separately in the local development environment.
