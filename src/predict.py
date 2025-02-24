#!/usr/bin/env python3
from core.training.train import train_model
import sys
import json
from core.training.train import sigmoid_function

def predict(X, weights):
    predict = weights[0]
    for i in range(1, len(X)):
        predict += X[i] * weights[i]
    return 1 if sigmoid_function(predict) >= 0.5 else 0 


if __name__ == "__main__":
    dataset = 'data/dataset_train.csv'
    if (len(sys.argv) != 1):
        print("")
        print("Usage: ./logreg_train.py")
        sys.exit(1)
    with open("logistic_regression_model.json", "r") as f:
        trained_models = json.load(f)
    