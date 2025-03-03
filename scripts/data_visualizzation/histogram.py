#!/usr/bin/env python3

import os
import sys

def set_path () : 
    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    sys.path.append(ROOT_DIR)
    print(ROOT_DIR)

if "/script/" in os.path:
    set_path()

from src.core.plots.plots import histogram_plot

if __name__ == "__main__":
    dataset = 'data/dataset_train.csv'
    if (len(sys.argv) != 1):
        print("The task is to identify the distibution of the data between all houses in the dataset and find the subject where it is evenly distributed.")
        print("Usage: ./histogram.py")
        sys.exit(1)
    histogram_plot(dataset)