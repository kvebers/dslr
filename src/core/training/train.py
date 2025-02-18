from ..description.operation import clean_data_and_feed_it_francesco
import copy

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
learning_rate = 0.001
epochs = 10000

def prep_data_for_each_house(data, house):
    # data = [row for row in data if row[0] == house row[0] = 1 else row[0] = 0]
    new_data = copy.deepcopy(data)
    for row in new_data:
        if row[0] == house:
            row[0] = 1
        else:
            row[0] = 0
    return new_data


def train_for_each_house(data):
    for house in houses:
        house_data = prep_data_for_each_house(data, house)
        for i in range(epochs):
            for row in house_data:
                for element in range(1, len(row)):
                    pass
        


def train_model(dataset_name):
    array_of_names = ["Index", "First Name", "Last Name", "Birthday", "Best Hand", "Arithmancy", "Care of Magical Creatures"]
    data, header = clean_data_and_feed_it_francesco(dataset_name, array_of_names)
    train_for_each_house(data)