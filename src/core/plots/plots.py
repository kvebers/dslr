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
    data = [element for element in data if element != '' or element != a.empty]
    return pd.DataFrame(data) 


def hands_data(data):
    data = [1 if element == 'Left' else 0 if element == 'Right' else ' ' for element in data]
    return pd.DataFrame(data)




# Vienmērīgais sadalījums varbūtību teorijā ir nepātraukts varbūtību sadalījums.
# Vienmērīgi sadalīts gadījuma lielums pieņem vērtības
# galīgā intervālā un tā blīvuma funkcija šajā intervālā ir konstanta.
# Tas nozīmē, ka jebkuriem apakšintervāliem ar vienādu garumu piemīt vienāda varbūtība.

# TLDR: If the data is uniformly distributed,
# the data will be similar for each course for each house -> as in function below
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
            ax.hist(scores_in_particular_course, bins=25, alpha=0.5, label=house, density=True)
            ax.set_title(f"{course}")
            ax.legend()
    plt.tight_layout()
    plt.show()



def scatter_plot(dataset):
    data = pd.read_csv(dataset)
    courses = data.columns[6:]
    new_courses = normalize_data(data[courses])
    fig, axes = plt.subplots(len(courses), len(courses), figsize=(6, 4))
    axes = axes.flatten()
    for i, course in enumerate(courses):
        ax = axes[i]
        for j, other_course in enumerate(courses):
            ax = axes[i * len(courses) + j]
            ax.scatter(new_courses[course], new_courses[other_course], alpha=0.5, color='red')
            ax.set_title(f"{course[:3]} vs {other_course[:3]}")
            ax.legend()
    plt.show()


def pair_scatter_histogram_plot(dataset):
    data = pd.read_csv(dataset)
    courses = data.columns[6:]
    houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
    new_courses = normalize_data(data[courses])
    fig, axes = plt.subplots(len(courses), len(courses), figsize=(6, 4))
    axes = axes.flatten()
    for i, course in enumerate(courses):
        ax = axes[i]
        for j, other_course in enumerate(courses):
            ax = axes[i * len(courses) + j]
            if (i == j):
                for house in houses:
                    data_regarding_house = data[data['Hogwarts House'] == house]
                    scores_in_particular_course = new_courses[course][data['Hogwarts House'] == house]
                    scores_in_particular_course = clean_data(scores_in_particular_course)
                    ax.hist(scores_in_particular_course, bins=25, alpha=0.5, label=house, density=True)
                    ax.set_title(f"{course}")
            else:
                ax.scatter(new_courses[course], new_courses[other_course], alpha=0.5, color='red')
                ax.legend()
                ax.set_title(f"{course[:3]} vs {other_course[:3]}")
    plt.show()

