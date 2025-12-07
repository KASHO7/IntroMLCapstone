import json
import os

def save_metrics(model_name, mse, rmse, mae,r2):

    metrics_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..",  "metrics")
    os.makedirs(metrics_dir, exist_ok=True)

    metrics = {
        "mse": mse,
        "rmse": rmse,
        "mae": mae,
        "r2": r2,
    }

    file_name = model_name.lower().replace(" ", "_")
    file_path = os.path.join(metrics_dir, f"{file_name}.json")

    with open(file_path, "w") as f:
        json.dump(metrics, f)

    print(f"Saved metrics to {file_path}")