<<<<<<< HEAD
# smart-fram-crop-reco
=======
# AI-Powered Crop Assistant System for India: District and Month-Specific Insights for Optimized Agricultural Practices

## Overview

This project develops an AI-driven crop recommendation system tailored for Indian farmers. By analyzing key environmental factors like temperature, humidity, pH, and rainfall, the system provides district and month-specific crop recommendations. The primary goal is to empower farmers with data-driven insights, enhancing agricultural productivity and sustainability across India. The system ranks the best crops to plant based on given conditions, facilitating informed decision-making for optimized farming practices.

## Features

- **Data Preprocessing**: Handles missing values, detects and manages outliers, normalizes/standardizes features, and encodes categorical data.
- **Model Training**: Trains multiple machine learning models: Decision Tree, Gaussian Naive Bayes, Support Vector Machine (SVM), Logistic Regression, Random Forest, XGBoost, and K-Nearest Neighbors (KNN).
- **Model Evaluation**: Evaluates models using accuracy, precision, recall, and F1 score. Calculates accuracies for each crop.
- **Visualization**: Visualizes model accuracies for each crop using Seaborn and Matplotlib.
- **Deployment**: Deploys the application on Streamlit Cloud for real-time crop recommendations.

## Usage

1. Ensure `Combined_Crop_recommendation.parquet` is in the same directory as `app.py`.
2. Run the Streamlit application:
   ```sh
   streamlit run app.py
   ```
3. Access the application in your web browser at `http://localhost:8501`.

## Project Structure

```
.
├── app.py                      # Streamlit application code
├── requirements.txt            # List of dependencies
├── Combined_Crop_recommendation.parquet  # Combined dataset
└── README.md                   # Project documentation
```

## Data Preprocessing

- **Missing Data**: Identifies and handles missing values appropriately.
- **Outliers**: Detects and manages outliers to prevent skewed results.
- **Feature Scaling**: Normalizes or standardizes features for consistent input scales.
- **Encoding Categorical Data**: Converts categorical variables to numerical values (e.g., one-hot encoding, label encoding).
- **Feature Engineering**: Creates or modifies features to improve data pattern capture.

## Model Training and Evaluation

- **Train-Test Split**: Splits data into training and testing sets to prevent overfitting.
- **Model Selection**: Chooses appropriate machine learning models for the task.
- **Hyperparameter Tuning**: Optimizes model performance by fine-tuning hyperparameters.
- **Model Evaluation**: Evaluates model performance using appropriate metrics. Employs cross-validation for consistent performance across data subsets.
- **Model Interpretation**: Understands feature contributions to model predictions.

## Visualization

- **Model Accuracies**: Visualizes the accuracies of all models for each crop using Seaborn and Matplotlib.

## Deployment

- **Streamlit Cloud**: Deploys the application on Streamlit Cloud for real-time crop recommendations.
