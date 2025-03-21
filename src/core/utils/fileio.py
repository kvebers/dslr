import os
import json
from core.const import MODEL_NAME

def read_dataset(dataset) -> tuple[list, list]:
    """
        This function takes a path to a file. Open it and returns:
            - Header: Name of the Columns in the Datasets.
            - Data: All the entry(row) in the Dataset.
    """
    data = []
    header = []
    with open(dataset) as f:
        for index, line in enumerate(f):
            line = line.strip()
            line = line.replace(',,', ', ,')
            row = line.split(',')
            if index == 0:
                header = row
                continue
            data.append(row)
    return data, header


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
        with open(f"./models/{MODEL_NAME}.json", "w") as f:
            json.dump(models, f)
    except Exception as e:
        print(f"Error: {e}")
        return False
    return True