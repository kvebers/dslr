#!/usr/bin/env python3
from core.training.train import train_model
from core.utils.fileio import save_model
import sys


if __name__ == "__main__":
    dataset = 'data/dataset_train.csv'
    if (len(sys.argv) != 1):
        print("""The task is to identify the distibution of the data
                between all houses in the dataset and find the subject
                where it is evenly distributed.""")
        print("Usage: ./logreg_train.py")
        sys.exit(1)
    models = train_model(dataset)
    if save_model(models) == False:
        print("Error in saving models.")
    else:
        print ("Model saved in ./models/")