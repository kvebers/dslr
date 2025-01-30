import pandas as pd
import matplotlib.pyplot as plt
from ..description.operation import get_max
from ..description.operation import get_min


def my_pandas_min_max_normalization(column):
    min_val = get_min(column)
    max_val = get_max(column)
    return (column - min_val) / (max_val - min_val) if max_val != min_val else column

#numbers = [1, 2, 3, 4, 5]
#squared_numbers = list(map(lambda x: x ** 2, numbers)) takes each element of numbers, squares it and returns a new list with the squared numbers.
def normalize_data(data):
    return data.apply(lambda column: my_pandas_min_max_normalization(column))


def clean_data(data):
    data = [element for element in data if element != '' or element != ' ']
    return pd.DataFrame(data) 

def histogram_plot(dataset):
    data = pd.read_csv(dataset)
    houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
    courses = data.columns[6:]
    new_courses = normalize_data(data[courses])
    fig, axes = plt.subplots(int((len(courses) + 2) / 3), 3, figsize=(8, 4))
    axes = axes.flatten()
    for i, course in enumerate(courses):
        ax = axes[i]
        for house in houses:
            data_regarding_house = data[data['Hogwarts House'] == house]
            scores_in_particular_course = new_courses[course][data['Hogwarts House'] == house]
            scores_in_particular_course = clean_data(scores_in_particular_course)
            ax.hist(scores_in_particular_course, bins=20, alpha=0.5, label=house, density=True)
            ax.set_title(f"{course}")
            ax.legend()
    plt.tight_layout()
    plt.show()