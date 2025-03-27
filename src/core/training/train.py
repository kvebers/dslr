from core.utils.dataset_operation import clean_data_and_normalize
import copy
import math
import random
import matplotlib.pyplot as plt


houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
learning_rate = 0.03
epochs = 50

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


# def gradient_descend(row, l_value, weights):
#     error = l_value - row[0]
# #    print(f"Prediction {row[0]} {1 if l_value > 0.5 else 0}")
#     for element in range(1, len(row)):
#         gradient = error * row[element]
#         weights[element] = weights[element] - gradient * learning_rate
#     return weights


def train_for_each_house(data):
    model = []
    fig, axes = plt.subplots(2, 2, figsize=(16, 8))
    axes = axes.flatten() 
    for plot_id, house in enumerate(houses):
        house_data = prep_data_for_each_house(data, house)
        weights = [i / 1000 * (-1)**i  for i in range(len(data[0]))]
        plot_data = []
        for i in range(epochs):
            random.shuffle(house_data)
            correct = 0
            error = [0 for j in range(len(data[0]))]
            for index, row in enumerate(house_data):
                predict = 0
                for element in range(1, len(row)):
                    predict += row[element] * weights[element]                
                logistic_value = sigmoid_function(predict)
                pred_error = logistic_value - row[0]
                if (pred_error < 0.3):
                    correct += 1
                for element in range(1, len(row)):
                    error[element] += pred_error * row[element]
                if index % 20 == 0:
                    for element in range(1, len(row)):
                        weights[element] -= (error[element] / 20) * learning_rate
            if (len(house_data) % 20 != 0):
                for element in range(1, len(row)):
                    weights[element] -= (error[element] / (len(house_data)  % 20)) * learning_rate
            plot_data.append(correct / len(house_data) * 100)
        axes[plot_id].plot(range(epochs), plot_data, label=f"House {house}")
        axes[plot_id].set_title(f"House {house}")
        axes[plot_id].set_xlabel("epochhh")
        axes[plot_id].set_ylabel("accuracy")
        axes[plot_id].legend()
        model.append(weights)
    plt.tight_layout()
    plt.show()
    return model


def train_model(dataset_name):
    columns_to_remove = [
    "Index",
    "First Name",
    "Last Name",
    "Birthday",
    "Best Hand",
    ]
    data, header = clean_data_and_normalize(dataset_name, columns_to_remove, 1)
    with open("validate.txt", "w") as file:
        for item in data:
            file.write(f"['{item[0]}']\n")
    model = train_for_each_house(data)
    return [header] + model[:]
