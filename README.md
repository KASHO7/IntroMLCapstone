
## Implementation and Models

This project implements five regression models for comparison, following the methodology described in the technical report.

### Models Implemented

| Category | Model | Implementation File | Key Technical Detail |
| :--- | :--- | :--- | :--- |
| **Baseline Algorithms** | **Linear Regression** | `linear_regression.ipynb` | Standard linear model used as the performance floor. |
| | **Polynomial Regression** | `polynomial_regression.ipynb` | Extends linearity using feature expansion ($\texttt{degree=3}$). |
| | **Multi-Layer Perceptron (MLP)** | `neural_network.ipynb` | Shallow Neural Network baseline, tuned using Randomized Search. |
| **Advanced Research Algorithms** | **Extreme Gradient Boosting (XGBoost)** | `XGBoost.ipynb` | Tree-based ensemble with explicit L1/L2 regularization ($\texttt{reg\_alpha}/\texttt{reg\_lambda}$). |
| | **Stacked Regression Meta-Model** | `stacking_regression.ipynb` | Ensemble combining diverse base models (Ridge, Lasso, SVR, ElasticNet) with a **RandomForest Meta-Learner**. |

-----

## Code Workflow

The project execution is organized into distinct phases using six notebooks and helper functions in the `utils` folder, demonstrating a clean, modular pipeline.

1.  **Preprocessing (`preprocessing.py`):**
      * Defines the $\texttt{load\_and\_transform}$ function, which handles data loading, train/test split, and **IQR-based outlier removal**.
      * Defines the $\texttt{preprocessing\_data}$ function, which sets up the $\texttt{ColumnTransformer}$ for consistent scaling and encoding across all models.
2.  **Model Training (5 Notebooks):**
      * Each of the five model notebooks (e.g., `XGBoost.ipynb`) trains its respective model, evaluates it, and calculates metrics.
3.  **Metrics Saving (`save_metrics.py`):**
      * Saves the calculated metrics ($R^2$, RMSE, MSE, MAE) to individual JSON files in the `metrics` folder.
4.  **Final Comparison (`compare_models.ipynb`):**
      * Loads all JSON metric files to generate the final comparison tables and visual plots (e.g., Figures 1 and 2 in the report).

-----

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/IntroMLCapstone.git
    ```
2.  **Install dependencies:** Ensure necessary packages, including **scikit-learn**, **xgboost**, **pandas**, **numpy**, **matplotlib**, and **seaborn**, are installed.
3.  **Run the analysis:** Execute the model notebooks sequentially, followed by $\texttt{compare\_models.ipynb}$ to reproduce the results and generate the final analysis.
