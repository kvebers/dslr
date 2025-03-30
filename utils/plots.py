import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from operation import get_max
from operation import get_min
from const import HOUSES, COLORS



def my_pandas_min_max_normalization(column):
    min_val = get_min(column)
    max_val = get_max(column)
    return (column - min_val) / (max_val - min_val) if max_val != min_val else column

#numbers = [1, 2, 3, 4, 5]
#squared_numbers = list(map(lambda x: x ** 2, numbers)) takes each element of numbers, squares it and returns a new list with the squared numbers.
def normalize_data_lazy(data):
    return data.apply(lambda column: my_pandas_min_max_normalization(column))

# TO CHECK THIS ONES 
def clean_data(data):
    data = [element for element in data if element != '' or element != a.empty]
    return pd.DataFrame(data) 


def hands_data(data):
    data = [1 if element == 'Left' else 0 if element == 'Right' else ' ' for element in data]
    return pd.DataFrame(data)


# TLDR: If the data is uniformly distributed,
# the data will be similar for each course for each house -> as in function below
def histogram_plot(dataset):
    data = pd.read_csv(dataset)
    courses = data.columns[6:]
    new_courses = normalize_data_lazy(data[courses])
    fig, axes = plt.subplots(int((len(courses) + 2) / 3), 3, figsize=(8, 4))
    axes = axes.flatten()
    for i, course in enumerate(courses):
        ax = axes[i]
        for house in HOUSES:
            data_regarding_house = data[data['Hogwarts House'] == house]
            scores_in_particular_course = new_courses[course][data['Hogwarts House'] == house]
            scores_in_particular_course = clean_data(scores_in_particular_course)
            ax.hist(scores_in_particular_course, bins=25, alpha=0.5, label=house, density=True, color=COLORS[house])
            ax.set_title(f"{course}")
    axes[0].legend(loc='upper right', bbox_to_anchor=(0.0, 0.0))
    plt.show()


def extract_months(data):
    return pd.to_datetime(data).dt.month

def extract_years(data):
    return pd.to_datetime(data).dt.year

def extract_days(data):
    return pd.to_datetime(data).dt.day


def normalize_houses(data):
    return data.apply(lambda x: HOUSES.index(x))

def scatter_plot(dataset):
    data = pd.read_csv(dataset)
    data["Hand Normalized"] = hands_data(data["Best Hand"])
    data["Months"] = extract_months(data["Birthday"])
    data["Years"] = extract_years(data["Birthday"])
    data["Days"] = extract_days(data["Birthday"])
    data["House Normalized"] = normalize_houses(data["Hogwarts House"])
    courses = data.columns[6:]
    new_courses = normalize_data_lazy(data[courses])
    fig, axes = plt.subplots(len(courses), len(courses), figsize=(16, 10))
    axes = axes.flatten()
    for i, course in enumerate(courses):
        for j, other_course in enumerate(courses):
            ax = axes[i * len(courses) + j]
            for house in HOUSES:
                color = COLORS[house]
                house_data = data[data['Hogwarts House'] == house]
                x_axis_scores = clean_data(new_courses[course][data['Hogwarts House'] == house])
                y_axis_scores = clean_data(new_courses[other_course][data['Hogwarts House'] == house])
                ax.scatter(x_axis_scores, y_axis_scores, alpha=0.25, label=house, color=color)
            ax.set_title(f"{course[:3]} vs {other_course[:3]}")
    axes[0].legend(loc='upper right', bbox_to_anchor=(0.0, 0.0))
    plt.show()
    fig, axes = plt.subplots(5, 1, figsize=(8, 4))
    axes = axes.flatten()
    for house in HOUSES:
        ax = axes[0]
        color = COLORS[house]
        ax.scatter(new_courses['Astronomy'], new_courses['Defense Against the Dark Arts'], alpha=0.5, color=color, label=house)
        ax.set_title("Answer: Astronomy vs Defense Against the Dark Arts")
    for i, house in enumerate(HOUSES):
        color = COLORS[house]
        ax = axes[i + 1]
        house_data = data[data['Hogwarts House'] == house]
        ax.scatter(house_data['Astronomy'], house_data['Defense Against the Dark Arts'], alpha=0.5, color=COLORS[house], label=house)
        ax.set_title(f"{house}")
    axes[0].legend(loc='upper right', bbox_to_anchor=(0.0, 0.0))
    plt.show()


def pair_scatter_histogram_plot(dataset):
    data = pd.read_csv(dataset)
    courses = data.columns[6:]
    new_courses = normalize_data_lazy(data[courses])
    fig, axes = plt.subplots(len(courses), len(courses), figsize=(16, 10))
    axes = axes.flatten()
    for i, course in enumerate(courses):
        ax = axes[i]
        for j, other_course in enumerate(courses):
            ax = axes[i * len(courses) + j]
            for house in HOUSES:
                if (i == j):
                    data_regarding_house = data[data['Hogwarts House'] == house]
                    scores_in_particular_course = new_courses[course][data['Hogwarts House'] == house]
                    scores_in_particular_course = clean_data(scores_in_particular_course)
                    ax.hist(scores_in_particular_course, bins=25, alpha=0.5, label=house, density=True, color=COLORS[house])
                    ax.set_title(f"{course}")
                else:
                    color = COLORS[house]
                    house_data = data[data['Hogwarts House'] == house]
                    x_axis_scores = clean_data(new_courses[course][data['Hogwarts House'] == house])
                    y_axis_scores = clean_data(new_courses[other_course][data['Hogwarts House'] == house])
                    ax.scatter(x_axis_scores, y_axis_scores, alpha=0.5, label=house, color=color)
                    ax.set_title(f"{course[:3]} vs {other_course[:3]}")
    axes[0].legend(loc='upper right', bbox_to_anchor=(0.0, 0.0))
    plt.tight_layout()
    plt.show()

