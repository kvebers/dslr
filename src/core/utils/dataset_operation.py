from core.utils.fileio import read_dataset
from core.utils.operation import (get_std, 
                                  get_mean, 
                                  get_count, 
                                  get_max, 
                                  get_min,
                                  normalize_data
                                  )
from core.utils.data_validation import check_if_can_calculate_mean


def get_column(dataset, column, header):
    col = header.index(column)
    return [row[col] for row in dataset]


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


def remove_empty_rows(dataset):
    with open('test.out', 'w') as f:
        f.write(str(dataset))
    new_dataset = []
    for row in dataset:
        if all(cell != '' and cell != ' ' for cell in row):
                new_dataset.append(row)
    return new_dataset


def clean_data_and_normalize(dataset, headers_to_remove):
    cleaned_dataset, header = remove_columns(dataset, headers_to_remove)
    new_dataset = remove_empty_rows(cleaned_dataset)
    normalize_data(new_dataset, header)
    return new_dataset, header


