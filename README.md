# Comparative Analysis of Regression Algorithms for House Price Prediction

This repository contains the complete implementation, analysis, and results for a capstone project focused on predicting housing prices using the Ames Housing Dataset. The project compares traditional machine learning baselines against modern ensemble and neural network techniques to determine the optimal predictive model.

-----

## Repository Structure

The project code and metrics are organized into the following directories:

```
Capstone_Project/
├── data/                    # Contains the raw dataset (train.csv, test.csv) and descriptive files.
├── metrics/                 # Stores JSON files (e.g., linear_regression.json) containing performance metrics (MSE, R2, RMSE, MAE) for each model.
├── models/                  # Contains all six main Jupyter Notebooks (.ipynb) for training and comparison.
├── utils/                   # Python helper functions and preprocessing pipelines.
└── README.md
```

-----

## Implementation and Models

This project implements five regression models for comparison, following the methodology described in the technical report.

### Models Implemented

| Category | Model | Implementation File | Key Technical Detail |
| :--- | :--- | :--- | :--- |
| **Baseline Algorithms** | Linear Regression | `linear_regression.ipynb` | Standard linear model used as the performance floor. |
| | Polynomial Regression | `polynomial_regression.ipynb` | Extends linearity using feature expansion ($\texttt{degree=3}$). |
| | Multi-Layer Perceptron (MLP) | `neural_network.ipynb` | Shallow Neural Network baseline, tuned using Randomized Search. |
| **Advanced Research Algorithms** | Extreme Gradient Boosting (XGBoost) | `XGBoost.ipynb` | Tree-based ensemble with explicit L1/L2 regularization ($\texttt{reg\_alpha/reg\_lambda}$). |
| | Stacked Regression Meta-Model | `stacking_regression.ipynb` | Ensemble combining diverse base models (Ridge, Lasso, SVR, ElasticNet) with a **RandomForest Meta-Learner**. |

### Code Workflow

The project execution is organized into distinct phases using six notebooks and the helper functions in the $\texttt{utils}$ folder:

1.  **Preprocessing ($\texttt{preprocessing.py}$):**
      * Defines the $\texttt{load\_and\_transform}$ function, which handles data loading, train/test split, and **IQR-based outlier removal**.
      * Defines the $\texttt{preprocessing\_data}$ function, which sets up the $\texttt{ColumnTransformer}$ for consistent scaling and encoding.
2.  **Model Training (5 Notebooks):**
      * Each of the five model notebooks (e.g., `XGBoost.ipynb`) trains its respective model, evaluates it, and calculates metrics.
3.  **Metrics Saving ($\texttt{save\_metrics.py}$):**
      * Saves the calculated metrics ($R^2$, RMSE, MSE, MAE) to individual JSON files in the $\texttt{metrics}$ folder.
4.  **Final Comparison ($\texttt{compare\_models.ipynb}$):**
      * Loads all JSON metric files to generate the final comparison tables and visual plots (e.g., Figures 1 and 2 in the report).

-----

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone https://github.com//IntroMLCapstone.git
    ```
2.  **Install dependencies:** Ensure necessary packages, including $\texttt{scikit-learn}$, $\texttt{xgboost}$, $\texttt{pandas}$, $\texttt{numpy}$, $\texttt{matplotlib}$, and **$\texttt{seaborn}$**, are installed.
3.  **Run the analysis:** Execute the model notebooks sequentially, followed by $\texttt{compare\_models.ipynb}$ to reproduce the results and generate the final analysis.
