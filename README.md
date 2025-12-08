IntroMLCapstone/
│
├── data/
│   └── house_prices.csv                # Ames Housing Dataset (Used for model training)
│
├── models/
│   ├── linear_regression.ipynb         # Baseline Linear Regression model
│   ├── polynomial_regression.ipynb     # Polynomial Regression (degree-based feature expansion)
│   ├── neural_network.ipynb            # MLP Neural Network implementation
│   ├── xgboost.ipynb                   # Extreme Gradient Boosting model
│   ├── stacking.ipynb                  # Stacked Regression Meta-Model
│   └── compare_models.ipynb            # Loads JSON metrics + generates comparison plots and tables
│
├── utils/
│   ├── preprocessing.py                # load_and_transform() + preprocessing_data() column transformer
│   └── save_metrics.py                 # Writes model metrics (MSE, RMSE, MAE, R²) into /metrics
│
├── metrics/
│   ├── linear_regression.json          # Saved performance metrics per model
│   ├── polynomial_regression.json
│   ├── neural_network.json
│   ├── xgboost.json
│   ├── stacking.json
│   └── README.md                       # (Optional) Explanation of how metrics are used
│
│
└── README.md                           # Project overview, instructions, documentation
