# LAB 12 - Monitoring, Drift Management and Continuous ML Systems

## Aim
To monitor the machine learning system, detect data and concept drift, evaluate model performance, automate retraining, and manage model versions using MLflow.

## Implementation
1. Implemented data drift detection using statistical comparison.
2. Implemented concept drift analysis using model performance metrics.
3. Monitored prediction and probability distributions.
4. Implemented API performance monitoring and inference logging.
5. Evaluated model performance across different data splits.
6. Retrained the model using updated training data.
7. Compared the baseline and retrained models.
8. Registered the retrained model in MLflow.

## Experimental Results

### Data Drift
- MonthlyCharges KS statistic: 0.158268
- TotalCharges KS statistic: 0.103593
- 2 out of 6 features showed drift.

### Model Comparison

| Metric | V1 | V2 |
|---|---:|---:|
| Accuracy | 0.7630 | 0.7715 |
| Precision | 0.5427 | 0.5542 |
| Recall | 0.6791 | 0.7112 |
| F1 Score | 0.6033 | 0.6230 |
| ROC-AUC | 0.8301 | 0.8361 |

### API Monitoring
- Total requests: 622
- Successful requests: 554
- Failed requests: 68
- Average latency: 68.437 ms
- P95 latency: 184.197 ms

### MLflow Registry
- Model V1 remains in Production.
- Model V2 is registered in Staging as version 8.
- Automatic promotion to Production was not performed.

## Result
Successfully implemented monitoring, drift detection, performance evaluation, model retraining and MLflow registry management.
