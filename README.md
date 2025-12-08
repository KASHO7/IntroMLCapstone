Comparative Analysis of Regression Algorithms for House Price Prediction

This repository contains the complete implementation, analysis, and results for a capstone project focused on predicting housing prices using the Ames Housing Dataset. The project compares traditional machine learning baselines against modern ensemble and neural network techniques to determine the optimal predictive model.
Project Objective

The primary goal was to implement and evaluate five distinct machine learning models—three baselines and two research-based advanced models—to establish which architecture provides the best prediction accuracy (R2 and RMSE) on a real-world, highly featured dataset.
Repository Structure

The project code and metrics are organized into the following directories:

Capstone_Project/
├── data/                    # Raw and description files (train.csv, test.csv)
├── metrics/                 # Stores JSON files containing performance metrics (MSE, R2, RMSE) for each model.
├── models/                  # Contains all main analysis notebooks and the final comparison notebook.
├── utils/                   # Python helper functions and preprocessing pipelines.
└── README.md

Implementation and Models

This project implements five regression models for comparison, following the methodology described in the technical report.
Models Implemented
Category	Model	Implementation File	Key Technical Detail
Baseline Algorithms	Linear Regression	linear_regression.ipynb	Standard linear model used as the performance floor.
	Polynomial Regression	polynomial_regression.ipynb	Extends linearity using feature expansion (degree=3).
	Multi-Layer Perceptron (MLP)	neural_network.ipynb	Shallow Neural Network baseline, tuned using Randomized Search.
Advanced Research Algorithms	Extreme Gradient Boosting (XGBoost)	XGBoost.ipynb	Tree-based ensemble with explicit L1/L2 regularization (reg_alpha/reg_lambda) for robustness.
	Stacked Regression Meta-Model	stacking_regression.ipynb	Ensemble technique combining diverse base models (Ridge, Lasso, SVR, ElasticNet) with a RandomForest Meta-Learner.
