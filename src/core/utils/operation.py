def get_count(row):
    count = 0
    for element in row:
        if (element != ' '):
            count += 1
    if (count == 0):
        return 0
    return count


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


def bubble_sort(dataset):
    for i in range(len(dataset)):
        for j in range(len(dataset) - 1):
            if dataset[j] > dataset[j + 1]:
                dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]
    return dataset


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


def sort_data_and_get_percentile(dataset, percentile):
    dataset = [float(x) for x in dataset if x != ' ' and x != '']
    #dataset.sort() // xd speed performance, python loops are fast xd
    dataset = bubble_sort(dataset)
    index = int((percentile / 100) * len(dataset))
    if (index == len(dataset)):
        return 0
    return dataset[index]


def get_quartiles(dataset, header):
    from core.utils.dataset_operation import get_column
    from core.utils.data_validation import check_if_can_calculate_mean

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


def normalize_data(dataset, header):
    from core.utils.data_validation import check_if_can_calculate_mean
    from core.utils.dataset_operation import get_column

    new_dataset = dataset.copy()
    for i in range(len(header)):
        if check_if_can_calculate_mean(get_column(dataset, header[i], header)):
            column = get_column(dataset, header[i], header)
            min_value = get_min(column)
            max_value = get_max(column)
            for j in range(len(column)):
                if column[j] == '':
                    column[j] = 0
                new_dataset[j][i] = (float(column[j]) - min_value) / (max_value - min_value)
    return new_dataset