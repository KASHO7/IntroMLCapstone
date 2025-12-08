
---

## Folder Details

| Folder | Description |
|--------|------------|
| **/data** | Contains the Ames Housing dataset used for model training and evaluation. |
| **/models** | Holds six Jupyter notebooks — one per model + the comparison notebook. |
| **/utils** | Contains helper functions for preprocessing and exporting metrics. |
| **/metrics** | Stores JSON output from each model after evaluation for side-by-side comparison. |

---

## File Descriptions

| File | Purpose |
|------|--------|
| **linear_regression.ipynb** | Trains and evaluates a baseline Linear Regression model. |
| **polynomial_regression.ipynb** | Extends linear regression using degree-based polynomial feature expansion. |
| **neural_network.ipynb** | Implements an MLP Neural Network baseline using hidden layers + ReLU. |
| **xgboost.ipynb** | Implements XGBoost, a modern tree-boosting model with L1/L2 regularization. |
| **stacking.ipynb** | Implements Stacked Regression Meta-Model combining multiple models into an ensemble. |
| **compare_models.ipynb** | Loads saved metrics from `/metrics`, generates comparison tables and plots. |
| **preprocessing.py** | Contains `load_and_transform()` and `preprocessing_data()` used by all models. |
| **save_metrics.py** | Exports model evaluation results to JSON for documentation and comparison. |

---

## Dependencies Needed

Install these libraries before running:

```bash
pip install numpy pandas scikit-learn matplotlib seaborn xgboost
