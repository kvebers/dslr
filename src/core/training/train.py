from ..description.operation import clean_data_and_feed_it_francesco

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]


def prep_data_for_each_house(data, house):
    # data = [row for row in data if row[0] == house row[0] = 1 else row[0] = 0]
    for row in data:
        if row[0] == house:
            row[0] = 1
        else:
            row[0] = 0
    return data


def train_for_each_house(data):
    for house in houses:
        house_data = prep_data_for_each_house(data, house)
        print(house_data)
        


def train_model(dataset_name):
    array_of_names = ["Index", "First Name", "Last Name", "Birthday", "Best Hand", "Arithmancy", "Care of Magical Creatures"]
    data, header = clean_data_and_feed_it_francesco(dataset_name, array_of_names)
    train_for_each_house(data)