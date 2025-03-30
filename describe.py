#!/usr/bin/env python3

import sys
from utils.fileio import read_dataset
from utils.operation import get_quartiles
from utils.dataset_operation import ( 
        get_std_data,
        get_min_data,
        get_max_data,
        get_mean_data,
        get_count_data
)



def  execute_describe(dataset):
    dataset_values, header = read_dataset(dataset)
    new_header = ["Column"]
    new_header.extend(header)
    print(new_header)
    print(get_count_data(dataset_values, header))
    print(get_mean_data(dataset_values, header))
    print(get_std_data(dataset_values, header))
    print(get_min_data(dataset_values, header))
    print(get_max_data(dataset_values, header))
    v_25, v_50, v_75 = get_quartiles(dataset_values, header)
    print(v_25)
    print(v_50)
    print(v_75)


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: ./describe.py DATA_SET_NAME")
        sys.exit(1)
    execute_describe(sys.argv[1])