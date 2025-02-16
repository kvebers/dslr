#!/usr/bin/env python3

import os
import sys


def read_dataset(dataset):
    data = []
    header = []
    with open(dataset) as f:
        for index, line in enumerate(f):
            line = line.strip()
            line = line.replace(',,', ', ,')
            row = line.split(',')
            if index == 0:
                header = row
                continue
            data.append(row)
    return data, header

def get_column(dataset, column, header):
    col = header.index(column)
    return [row[col] for row in dataset]

def get_count(row):
    count = 0
    for element in row:
        if (element != ' '):
            count += 1
    if (count == 0):
        return 0
    return count


def get_count_data(dataset, header):
    count_row = ["Count"]
    for row in header:
        count_row.append(get_count(get_column(dataset, row, header)))
    return count_row


def get_mean(row):
    sum = 0
    count = 0
    for element in row:
        if element != ' ' and element != '':
            sum += float(element)
            count += 1
    if (count == 0):
        return 0
    return sum / count


def check_if_can_calculate_mean(row):
    for element in row:
        if element.strip() == '':
            continue
        try:
            float(element)
        except ValueError:
            return False
    return True


def get_mean_data(dataset, header):
    mean_row = ["Mean"]
    for row in header:
        if check_if_can_calculate_mean(get_column(dataset, row, header)):
            mean_row.append(get_mean(get_column(dataset, row, header)))
        else:
            mean_row.append('Not a float')
    return mean_row


def get_std(row):
    mean = get_mean(row)
    sum = 0
    count = 0
    for element in row:
        if element != ' ' and element != '':
            sum += (float(element) - mean) ** 2
            count += 1
    if (count == 0):
        return 0
    return (sum / count) ** 0.5


def get_std_data(dataset, header):
    std_row = ["Std"]
    for row in header:
        if check_if_can_calculate_mean(get_column(dataset, row, header)):
            std_row.append(get_std(get_column(dataset, row, header)))
        else:
            std_row.append('Not a float')
    return std_row


def get_min(row):
    min = float('inf')
    for element in row:
        if element != ' ' and element != '':
            if float(element) < min:
                min = float(element)
    return min


def get_max(row):
    max = float('-inf')
    for element in row:
        if element != ' ' and element != '':
            if float(element) > max:
                max = float(element)
    return max


def get_min_data(dataset, header):
    min_row = ["Min"]
    for row in header:
        if check_if_can_calculate_mean(get_column(dataset, row, header)):
            min_row.append(get_min(get_column(dataset, row, header)))
        else:
            min_row.append('Not a float')
    return min_row

def get_max_data(dataset, header):
    max_row = ["Max"]
    for row in header:
        if check_if_can_calculate_mean(get_column(dataset, row, header)):
            max_row.append(get_max(get_column(dataset, row, header)))
        else:
            max_row.append('Not a float')
    return max_row



def my_sort(dataset):
    for i in range(len(dataset)):
        for j in range(len(dataset) - 1):
            if dataset[j] > dataset[j + 1]:
                dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]
    return dataset


def sort_data_and_get_percentile(dataset, percentile):
    dataset = [float(x) for x in dataset if x != ' ' and x != '']
    #dataset.sort() // xd speed performance, python loops are fast xd
    dataset = my_sort(dataset)
    index = int((percentile / 100) * len(dataset))
    if (index == len(dataset)):
        return 0
    return dataset[index]


def get_quartiles(dataset, header):
    v_25 = ["25%"]
    v_50 = ["50%"]
    v_75 = ["75%"]
    for row in header:
        if check_if_can_calculate_mean(get_column(dataset, row, header)):
            v_25.append(sort_data_and_get_percentile(get_column(dataset, row, header), 25))
            v_50.append(sort_data_and_get_percentile(get_column(dataset, row, header), 50))
            v_75.append(sort_data_and_get_percentile(get_column(dataset, row, header), 75))
        else:
            v_25.append('Not a float')
            v_50.append('Not a float')
            v_75.append('Not a float')
    return v_25, v_50, v_75

def remove_columns(dataset, headers_to_remove):
    dataset_values, header = read_dataset(dataset)
    index_to_remove = [header.index(header_to_remove) for header_to_remove in headers_to_remove]
    index_to_remove.sort(reverse=True)
    header = [header[i] for i in range(len(header)) if i not in index_to_remove]
    cleaned_dataset = [[row[i] for i in range(len(row)) if i not in index_to_remove] for row in dataset_values]
    return cleaned_dataset, header

def remove_empty_rows(dataset):
    new_dataset = []
    for row in dataset:
        if all(cell != '' and cell != ' ' for cell in row):
            new_dataset.append(row)
    return new_dataset


def normalize_data(dataset, header):
    new_dataset = dataset.copy()
    for i in range(len(header)):
        if check_if_can_calculate_mean(get_column(dataset, header[i], header)):
            column = get_column(dataset, header[i], header)
            min_value = get_min(column)
            max_value = get_max(column)
            for j in range(len(column)):
                new_dataset[j][i] = (float(column[j]) - min_value) / (max_value - min_value)
    return new_dataset




def clean_data_and_feed_it_francesco(dataset, headers_to_remove):
    cleaned_dataset, header = remove_columns(dataset, headers_to_remove)
    new_dataset = remove_empty_rows(cleaned_dataset)
    normalize_data(new_dataset, header)
    return new_dataset, header

def  execute_describe(dataset):
    dataset_values, header = read_dataset(dataset)
    new_header = ["Column"]
    new_header.extend(header)
    print(new_header)
    print(get_count_data(dataset_values, header))
    print(get_mean_data(dataset_values, header))
    print(get_std_data(dataset_values, header))
    print(get_min_data(dataset_values, header))
    print(get_max_data(dataset_values, header))
    v_25, v_50, v_75 = get_quartiles(dataset_values, header)
    print(v_25)
    print(v_50)
    print(v_75)
    clean_data_and_feed_it_francesco(dataset, ["Index", "First Name", "Last Name", "Birthday", "Best Hand", "Arithmancy", "Care of Magical Creatures"])