from core.utils.dataset_operation import clean_data_and_normalize
import copy
import math

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
learning_rate = 0.001
epochs = 1000

def prep_data_for_each_house(data, house):
    # data = [row for row in data if row[0] == house row[0] = 1 else row[0] = 0]
    new_data = copy.deepcopy(data)
    for row in new_data:
        if row[0] == house:
            row[0] = 1
        else:
            row[0] = 0
    return new_data


# logistic_function
def sigmoid_function(prediction):
    return (1 / (1 + math.exp(-prediction)))    


def gradient_descend(row, l_value, weights):
    error = l_value - row[0]
    for element in range(1, len(row)):
        gradient = error * row[element]
        weights[element] = weights[element] - gradient * learning_rate 
    return weights


def train_for_each_house(data):
    model = []
    for house in houses:
        house_data = prep_data_for_each_house(data, house)
        weights = [0.0 for i in range(len(data[0]))]
        for i in range(epochs):
            for row in house_data:
                predict = 0
                for element in range(1, len(row)):
                    predict += row[element] * weights[element]
                logistic_value = sigmoid_function(predict)
                weights = gradient_descend( row, logistic_value, weights)
        model.append(weights)
    return model   


def train_model(dataset_name):
    columns_to_remove = ["Index", "First Name", "Last Name", "Birthday", "Best Hand", "Arithmancy", "Care of Magical Creatures"]
    data, header = clean_data_and_normalize(dataset_name, columns_to_remove)
    model = train_for_each_house(data)
    return [header] + model[:]
