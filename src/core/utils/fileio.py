import os
import json

def extract_input_from_file (filename :str = "dataset_train.csv") -> list :
    current_directory = str(os.getcwd())
    PATH = current_directory + "/data/" + filename
    value = []
    try:
        with open(PATH) as f:
            for line in f:
                value.append(str(line))
        return value
    except:
        return None


def save_model(models: list) -> bool:
    os.makedirs("./models", exist_ok=True)
    try:
        with open("./models/logistic_regression_model.json", "w") as f:
            json.dump(models, f)
    except Exception as e:
        print(f"Error: {e}")
        return False
    return True