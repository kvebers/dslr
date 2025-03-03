#!/usr/bin/env python3


import os
import sys

def set_path () : 
    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    sys.path.append(ROOT_DIR)
    print(ROOT_DIR)

if "/script/" in os.path:
    set_path()

from src.core.plots.plots import scatter_plot


if __name__ == "__main__":
    dataset = 'data/dataset_train.csv'
    if (len(sys.argv) != 1):
        print("Make a script called scatter_plot.[extension], which displays a scatter plot answering: \"What are the two features that are similar ?\"")
        print("Usage: ./scatter_plot.py")
        sys.exit(1)
    scatter_plot(dataset)

