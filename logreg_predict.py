#!/usr/bin/env python3
import sys
import json
from utils.train import sigmoid_function
from utils.dataset_operation import clean_data_and_normalize
from utils.const import ARRAY_OF_NAMES
from utils.train import houses


def compare_most_probable(preds :list) -> list:
    tmp_value = 0
    index_tmp = 0
    for index,value in enumerate(preds, 0):
        if float(value) > float(tmp_value):
            tmp_value = value
            index_tmp = index
    for index,value in enumerate(preds, 0):
        if index == index_tmp:
            preds[index] = 1
        else:
            preds[index] = 0
    return preds


def predict(X, houseModels):
    predict = []
    result = []
    for weights in houseModels:
        linear_combination = 0
        for i in range(1, len(X)):
            linear_combination += X[i - 1] * weights[i]
        predict.append(linear_combination)
    for value in predict:
        prob = sigmoid_function(value)
        result.append(prob)
    result = compare_most_probable(result)
    actual_result = []
    for index, value in enumerate(result, 0):
        if value == 1:
            actual_result.append(houses[index])
    return actual_result
            

if __name__ == "__main__":
    dataset = './data/dataset_train.csv'
    if (len(sys.argv) == 1):
        dataset = './data/dataset_test.csv'
    clean_data, header = clean_data_and_normalize(dataset, ARRAY_OF_NAMES, 0)
    try:
        with open("./models/logistic_regression_model.json", "r") as f:
            trained_models = json.load(f)
            tags = trained_models[0]
            houseModels = trained_models[1:]
        if (len(sys.argv) != 1):
            with open("validate/predictions.txt", "w") as file:
                for row in clean_data:
                    result = predict(row, houseModels)
                    file.write(f"{result[0]}\n")
        else:
            for row in clean_data:
                result = predict(row, houseModels)
                print(result[0])
    except:
        print("Something Went wrong")
