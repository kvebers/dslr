#!/usr/bin/env python3
from core.plots.plots import pair_scatter_histogram_plot
import sys




if __name__ == "__main__":
    dataset = 'data/dataset_train.csv'
    if (len(sys.argv) != 1):
        print("The task is to identify the distibution of the data between all houses in the dataset and find the subject where it is evenly distributed.")
        print("Usage: ./pair_plot.py")
        sys.exit(1)
    pair_scatter_histogram_plot(dataset)