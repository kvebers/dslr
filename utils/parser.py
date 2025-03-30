import sys
import os


sys.path.append(os.path.abspath(os.path.dirname(__file__)))


from fileio import extract_input_from_file

def extract_data_content(rows: list) -> list[dict]:
    keys = rows[0].split(",") 
    value = {}
    content = []
    for i in range(1, len(rows)):
        value = dict (zip ((keys), rows[i].split(",")))
        content.append(value)
    return content

def execute_parsing(dataset_name: str = "dataset_train.csv") -> list[dict]:
    content = extract_input_from_file(dataset_name)
    if content == None:
        return None, None
    return extract_data_content(content)

