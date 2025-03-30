#!/usr/bin/env python3
import os
import sys

from utils.plots import scatter_plot


if __name__ == "__main__":
    dataset = 'data/dataset_train.csv'
    if (len(sys.argv) != 1):
        print("Make a script called scatter_plot.[extension], which displays a scatter plot answering: \"What are the two features that are similar ?\"")
        print("Usage: ./scatter_plot.py")
        sys.exit(1)
    scatter_plot(dataset)

