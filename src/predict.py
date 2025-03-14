#!/usr/bin/env python3
from core.training.train import train_model
import sys
import json
from core.training.train import sigmoid_function
from core.utils.dataset_operation import clean_data_and_normalize
import pprint 

def predict(X, weights):
    
    predict = []
    result = []
    for weight in weights:
        product = 0
        for i in range(1, len(X)):
            product += X[i] * weight[i]
        predict.append(product)
    for value in predict:
        prob = sigmoid_function(value)
        result.append(prob) 
    # return result
    result = []
    for value in predict: 
        if sigmoid_function(value) >= 0.5:
            result.append('1')
        else:
            result.append('0')
    return result
            


if __name__ == "__main__":
    dataset = './data/dataset_test.csv'
    array_of_names = ["Index", "First Name", "Last Name", "Birthday", "Best Hand", "Arithmancy", "Care of Magical Creatures"]
    clean_data, header = clean_data_and_normalize(dataset, array_of_names)
    print("CLEAN_DATA")
    print(clean_data)
    if (len(sys.argv) != 1):
        print("")
        print("Usage: ./logreg_train.py")
        sys.exit(1)
    with open("./models/logistic_regression_model.json", "r") as f:
        trained_models = json.load(f)
        tags = trained_models[0]
        weights = trained_models[1:]
        for value in weights:
            pprint.pp(value)
    student_scores = [1, 8.5, 7.0, 9.0, 5.5, 6.0, 7.5, 8.0, 7.8, 8.2, 6.9, 5.0]
    for row in clean_data:
        result = predict(row, weights)
        print(result)


