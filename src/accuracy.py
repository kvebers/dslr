#!/usr/bin/env python3

valid_data = []
another_data = []


with open ('validate.txt', 'r') as f:
    for line in f:
        valid_data.append(line)

with open ('test.txt', 'r') as f:
    for line in f:
        another_data.append(line)

accuracy = 0
total = 0
for i in range(len(valid_data)):
    if valid_data[i] in another_data[i]:
        accuracy += 1
    total += 1

print(accuracy / total)