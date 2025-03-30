#!/usr/bin/env python3

valid_data = []
another_data = []


try:
    with open ('validate/validate.txt', 'r') as f:
        for line in f:
            valid_data.append(line)

    with open ('validate/predictions.txt', 'r') as f:
        for line in f:
            another_data.append(line)

    accuracy = 0
    total = 0
    if len(valid_data) != len(another_data):
        print("Error")
        exit(1)
    for i in range(len(valid_data)):
        if valid_data[i] in another_data[i]:
            accuracy += 1
        total += 1

    print(accuracy / total)
except:
    print("OKAY")