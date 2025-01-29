import pandas as pd
import matplotlib.pyplot as plt



def histogram_plot(dataset):
    data = pd.read_csv(dataset)
    houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
    courses = data.columns[6:]
    fix, axes = plt.subplots(len(courses), 1)
    axes = axes.flatten()
    for i, course in enumerate(courses):
        ax = axes[i]
        for house in houses:
            data_regarding_house = data[data['Hogwarts House'] == house]
            scores_in_particular_course = data_regarding_house[course]
            scores_in_particular_course = scores_in_particular_course.dropna()
            ax.hist(scores_in_particular_course, bins=20, alpha=0.5, label=house, density=True)
    plt.show()


