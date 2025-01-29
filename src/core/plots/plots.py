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

def histogram_plot(dataset):
    data = pd.read_csv(dataset)
    houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
    courses = data.columns[6:]
    new_courses = normalize_data(data[courses])
    new_courses.dropna()
    # fix, axes = plt.subplots(len(courses), 1)
    # axes = axes.flatten()
    # for i, course in enumerate(courses):
    #     ax = axes[i]
    #     for house in houses:
    #         data_regarding_house = data[data['Hogwarts House'] == house]
    #         scores_in_particular_course = data_regarding_house[course]
    #         scores_in_particular_course = scores_in_particular_course.dropna()
    #         ax.hist(scores_in_particular_course, bins=20, alpha=0.5, label=house, density=True)
    # plt.show()


