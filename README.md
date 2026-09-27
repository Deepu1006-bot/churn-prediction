# Customer Churn Prediction

## Project Overview

This project predicts whether a customer is likely to leave a service using machine learning techniques.

The project follows an MLOps workflow covering data preprocessing, model training, evaluation, experiment tracking, data validation, reproducible pipelines, and model registry lifecycle management.

## Objectives

- Predict customer churn
- Preprocess customer data
- Train and evaluate machine learning models
- Compare model performance using evaluation metrics
- Track experiments using MLflow
- Validate dataset schema and preprocessing outputs
- Build reproducible ML pipelines
- Register and version trained models
- Manage model lifecycle from Staging to Production
- Maintain model lineage and deployment metadata

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Pandera
- MLflow
- Matplotlib
- Joblib
- Jupyter Notebook
- Git & GitHub

## Project Structure

```text
churn-prediction/
|
|-- data/
|   |-- raw/
|   |   `-- churn.csv
|   `-- processed/
|       |-- X_train_final.npy
|       |-- X_test_final.npy
|       |-- y_train.npy
|       |-- y_test.npy
|       `-- dataset_metadata.json
|
|-- notebooks/
|   `-- project_implementation.ipynb
|
|-- pipelines/
|   |-- run_lab3_baseline.py
|   |-- run_lab4_tracking.py
|   |-- run_lab5_pipeline.py
|   `-- run_lab6_registry.py
|
|-- src/
|   |-- preprocess.py
|   |-- train.py
|   |-- evaluate.py
|   |-- train_mlflow.py
|   |-- validate_reproducibility.py
|   |-- validate_data.py
|   |-- preprocess_pipeline.py
|   |-- validate_outputs.py
|   |-- train_registry.py
|   |-- automate_lifecycle.py
|   `-- generate_registry_report.py
|
|-- models/
|   `-- preprocessor.pkl
|
|-- artifacts/
|   |-- preprocessing_summary_report.json
|   |-- baseline_validation.csv
|   `-- production_model_report.json
|
|-- mlruns/
|-- .gitignore
|-- README.md
`-- requirements.txt

Machine Learning Workflow
Raw Data
   |
   v
Data Validation
   |
   v
Data Preprocessing
   |
   v
Feature Preparation
   |
   v
Model Training
   |
   v
Model Evaluation
   |
   v
MLflow Experiment Tracking
   |
   v
Reproducibility Validation
   |
   v
Model Registry
   |
   v
Staging
   |
   v
Production

Lab 3 - Git-Based Version Control

Implemented:

Git repository initialization
Repository structure for ML projects
Version control of source code
Commit-based traceability
GitHub workflow
Baseline ML pipeline
Version-controlled ML project files
Lab 4 - Experiment Tracking and Reproducibility

Implemented:

MLflow experiment tracking
Parameter logging
Metric logging
Model artifact tracking
Preprocessing artifact tracking
Reproducibility validation
Experiment comparison
ML experiment lineage
Lab 5 - Data Validation and Reproducible ML Pipeline

Implemented:

Schema validation using Pandera
Data type validation
Categorical-value validation
Missing and invalid data checks
Train-test preprocessing pipeline
Numerical imputation
Feature scaling
Categorical encoding
Processed dataset generation
Preprocessing pipeline serialization
Output validation
Automated pipeline execution

Lab 5 Pipeline

validate_data.py
       |
       v
preprocess_pipeline.py
       |
       v
validate_outputs.py

The complete Lab 5 pipeline is executed using:

pipelines/run_lab5_pipeline.py

The pipeline validates the raw dataset, preprocesses the data, saves the preprocessing pipeline, generates processed datasets, and validates the final outputs.

Lab 6 - Model Registry and Lifecycle Management

Implemented:

Random Forest model training

MLflow model registration

Model versioning
Preprocessing dependency tracking
Model metadata tracking
Staging and Production lifecycle
Automated model promotion
Model performance comparison
Production model report generation
Model lineage tracking
Deployment readiness information

Lab 6 Pipeline

train_registry.py
       |
       v
automate_lifecycle.py
       |
       v
generate_registry_report.py

The complete Lab 6 pipeline is executed using:

pipelines/run_lab6_registry.py
Registered Model
Telco_Churn_Production_Model

Current Production Version

Version: 1
Stage: Production
Production Model Performance
Recall     : 0.6791
F1 Score   : 0.6033
ROC-AUC    : 0.8301
Accuracy   : 0.7630
Precision  : 0.5427

Model Hyperparameters

n_estimators : 200
max_depth    : 15
random_state : 42
class_weight : balanced
model_family : RandomForest
Model Lifecycle
New Model
    |
    v
MLflow Registry
    |
    v
Staging
    |
    v
Performance Evaluation
    |
    v
Production

The lifecycle manager evaluates staging candidates using recall and applies the defined promotion logic for moving models to Production.

Reproducibility

The project uses controlled preprocessing and fixed model configuration to support reproducible machine learning workflows.

Important configuration:

random_state = 42

A reproducibility validation script is included:

src/validate_reproducibility.py
Data Validation

The project uses Pandera for schema-aware validation of the Telco Customer Churn dataset.

Validation includes:

Column structure
Data types
Allowed categorical values
Numerical constraints
Dataset schema consistency

Validation results are stored as artifacts.

Preprocessing

The preprocessing workflow includes:

Conversion of TotalCharges to numeric values
Conversion of churn labels to binary values
Train-test splitting
Numerical imputation
Standard scaling
One-hot encoding
Saving the fitted preprocessing pipeline

The preprocessing pipeline is saved as:

models/preprocessor.pkl
Generated Artifacts

Important generated artifacts include:

artifacts/
|
|-- baseline_validation.csv
|-- preprocessing_summary_report.json
`-- production_model_report.json

The production model report contains model registry status, model version, stage, run information, performance metrics, hyperparameters, and preprocessing dependency information.

Deployment Readiness

The generated production registry report contains the status:

READY_FOR_DEPLOYMENT
Version Control

The project is maintained using Git and GitHub.

The implementation for Labs 3, 4, 5, and 6 is version controlled and pushed to the main branch.

Conclusion

This project demonstrates an end-to-end MLOps workflow for customer churn prediction, including version control, experiment tracking, reproducibility, data validation, automated preprocessing, model registration, lifecycle management, and production model traceability.