import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np


def load_and_trasnform(path):
    house_price_df = pd.read_csv(path)

    Q1 = np.percentile(house_price_df['SalePrice'], 25)
    Q3 = np.percentile(house_price_df['SalePrice'], 75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    house_price_df = house_price_df[(house_price_df['SalePrice'] >= lower) & (house_price_df['SalePrice'] <= upper)]

    #house_price_df = house_price_df.drop(columns=['Id'], errors='ignore')

    y = house_price_df["SalePrice"].values
    X = house_price_df.drop(columns=['SalePrice'])

    return X, y

def preprocessing_data(X):
    numeric_feature = X.select_dtypes(include=["int64", "float64"]).columns
    categoric_feature = X.select_dtypes(include=["object"]).columns

    num_transformer = Pipeline(steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())])
    cat_transformer = Pipeline(steps=[("imputer", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore"))])

    perprocessor_transformer = ColumnTransformer(transformers=[("num", num_transformer, numeric_feature), ("cat", cat_transformer, categoric_feature)])
    return perprocessor_transformer
