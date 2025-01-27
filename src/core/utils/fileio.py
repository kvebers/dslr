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
