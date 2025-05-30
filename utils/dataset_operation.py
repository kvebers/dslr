import sys
import os


sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from fileio import read_dataset
from operation import (get_std, 
                                  get_mean, 
                                  get_count, 
                                  get_max, 
                                  get_min,
                                  get_count,
                                  normalize_data,
                                  get_count_empty
                                  )
                                  
from data_validation import check_if_can_calculate_mean




def get_column(dataset, column, header):
    col = header.index(column)
    return [row[col] for row in dataset]


def count_empty_rows(dataset, header):
    min_row = ["Empty Cells"]
    for row in header:
        min_row.append(get_count_empty(get_column(dataset, row, header)))
    return min_row

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


def get_count_data(dataset, header):
    count_row = ["Count"]
    for row in header:
        count_row.append(get_count(get_column(dataset, row, header)))
    return count_row


def get_mean_data(dataset, header):
    mean_row = ["Mean"]
    for row in header:
        if check_if_can_calculate_mean(get_column(dataset, row, header)):
            mean_row.append(get_mean(get_column(dataset, row, header)))
        else:
            mean_row.append('Not a float')
    return mean_row


def get_std_data(dataset, header):
    std_row = ["Std"]
    for row in header:
        if check_if_can_calculate_mean(get_column(dataset, row, header)):
            std_row.append(get_std(get_column(dataset, row, header)))
        else:
            std_row.append('Not a float')
    return std_row


def remove_columns(dataset, headers_to_remove):
    dataset_values, header = read_dataset(dataset)
    index_to_remove = [header.index(header_to_remove) for header_to_remove in headers_to_remove]
    index_to_remove.sort(reverse=True)
    header = [header[i] for i in range(len(header)) if i not in index_to_remove]
    cleaned_dataset = [[row[i] for i in range(len(row)) if i not in index_to_remove] for row in dataset_values]
    return cleaned_dataset, header


# def remove_empty_rows(dataset):
#     new_dataset = []
#     for row in dataset:
#         if all(cell != '' and cell != ' ' for cell in row):
#             new_dataset.append(row)
#     return new_dataset


def remove_empty_rows(dataset):
    new_dataset = []
    sums = [0] * len(dataset[0])
    i = 0
    for row in dataset:
        for index, cell in enumerate(row):
            try:
                value = float(cell)
                sums[index] += value
            except:
                pass
        i += 1
    empty_cell_replacments = [(sums[index] / i) for index in range(len(sums))]
    for row in dataset:
        new = [f"{empty_cell_replacments[index]}" if (cell == "" or cell == " ") else cell for index, cell in enumerate(row)]
        new_dataset.append(new)
    return new_dataset


def clean_data_and_normalize(dataset, headers_to_remove, flag):
    cleaned_dataset, header = remove_columns(dataset, headers_to_remove)
    new_dataset = remove_empty_rows(cleaned_dataset)
    normalize_data(new_dataset, header, flag)
    return new_dataset, header


