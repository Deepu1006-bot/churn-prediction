# LAB 7 – MLOps Pipeline Implementation

## 1. Aim
To implement an end-to-end MLOps pipeline for Telco Customer Churn Prediction with data loading, data validation, preprocessing, model training, evaluation, quality checking, model lifecycle management, and inference.

## 2. Dataset
The project uses the Telco Customer Churn dataset stored at `data/raw/churn.csv`. The dataset contains 7,043 rows and 21 columns.

## 3. Pipeline Stages

1. **Data Loading:** Loads the raw churn dataset.
2. **Data Validation:** Checks the input dataset for data quality issues.
3. **Preprocessing:** Prepares the data for model training and saves the preprocessor.
4. **Output Validation:** Validates the processed outputs.
5. **Model Training and Registry:** Trains the churn prediction model and logs the experiment using MLflow.
6. **Model Evaluation:** Evaluates the model using accuracy, precision, recall, F1-score, and ROC-AUC.
7. **Quality Gate:** Checks whether the model meets the configured minimum F1-score.
8. **Model Lifecycle Management:** Evaluates the model and manages its registry stage.
9. **Inference:** Loads the Production model and generates predictions.
10. **Failure Injection:** Provides a script for testing failure-handling scenarios.

## 4. Configuration
The pipeline settings are maintained in `config.yaml`, including dataset paths, train-test split settings, model parameters, MLflow configuration, and the quality-gate threshold.

## 5. Tools and Technologies
- Python
- Pandas and Scikit-learn
- MLflow
- PyYAML
- Git and GitHub

## 6. Execution

Run the pipeline from the project root:

`python src/mlops_pipeline/churn_prediction_pipeline.py`

## 7. Observed Results
The pipeline completed successfully in the local environment.

- Dataset loaded: 7,043 rows and 21 columns.
- Accuracy: 0.7630
- Precision: 0.5427
- Recall: 0.6791
- F1-score: 0.6033
- ROC-AUC: 0.8301
- Quality gate: Passed because F1-score 0.6033 was greater than or equal to the configured threshold of 0.60.

The trained model was registered with MLflow. The tested model version was moved to Staging and subsequently archived because it did not improve upon the existing Production model.

## 8. Generated Outputs
- `models/churn_model.pkl`
- `models/preprocessor.pkl`
- `reports/evaluation_report.json`
- `reports/quality_gate_report.json`
- `outputs/inference_predictions.csv`
- `logs/churn_prediction_pipeline_run_log.json`

## 9. Conclusion
The end-to-end churn prediction pipeline executed successfully, covering data validation, preprocessing, model training, evaluation, quality gating, model lifecycle management, and inference.
