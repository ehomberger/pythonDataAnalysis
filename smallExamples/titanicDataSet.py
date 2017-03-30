# Visualizing data from the titanic
# Created by Eric Homberger

# Following loosely with Kaggle tutorial at https://www.kaggle.com/c/titanic and http://nbviewer.jupyter.org/gist/mwaskom/8224591

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# use pandas to import the data based on the url
url = "https://raw.github.com/mattdelhey/kaggle-titanic/master/Data/train.csv"
titanicData = pd.read_csv(url)

# adds a new column called pclass and maps it to class. Mapping goes (new column value):(old column value)
titanicData["class"] = titanicData.pclass.map({1: "First", 2: "Second", 3: "Third"})

# Return the data so I can play with it in the console
def returnData():
    return titanicData


def classBarPlot():
    # generates the barplot
    sns.barplot(titanicData["class"], titanicData["survived"], 
            x_order = ['First', 'Second', 'Third'])

    # shows the barplot
    plt.show()

def violinAge():
    sns.violinplot(x="class", y="age", hue="sex", data=titanicData, split=True,
                    inner="quart", palette={"male": "b", "female": "y"}) 
    plt.show()


def surviveBySex():
    plot = sns.factorplot(x="class", y="survived", hue="sex", data=titanicData,
            size=6, kind="bar", x_order = ['First', 'Second', 'Third'])
    
    plot.despine(left=True)
    
    plt.show(plot)


def addLastName():
    titanicData['last'] = titanicData['name'].str.split(' ').str.get(0)
