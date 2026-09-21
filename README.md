# Customer Churn Prediction

## 📌 Project Overview

This project predicts whether a customer is likely to leave a service using machine learning techniques.

The project follows a structured ML workflow including data preprocessing, model training, evaluation, and experiment tracking.

## 🎯 Objectives

- Predict customer churn
- Preprocess customer data
- Train multiple machine learning models
- Compare model performance
- Evaluate models using ROC-AUC and other metrics
- Track experiments using MLflow

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- MLflow
- Jupyter Notebook
- Git & GitHub

## 📂 Project Structure

```text
churn-prediction/
│
├── data/
│   └── raw/
│       └── churn.csv
│
├── notebooks/
│   └── project_implementation.ipynb
│
├── pipelines/
│   ├── run_lab3_baseline.py
│   └── run_lab4_tracking.py
│
├── src/
│   ├── evaluate.py
│   ├── preprocess.py
│   ├── train.py
│   └── train_mlflow.py
│
├── .gitignore
├── README.md
└── requirements.txt


Machine Learning Workflow


Raw Data
   ↓
Data Preprocessing
   ↓
Feature Preparation
   ↓
Model Training
   ↓
Model Evaluation
   ↓
ROC-AUC Comparison
   ↓
Experiment Tracking


