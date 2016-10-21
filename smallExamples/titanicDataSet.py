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

# prints some techincal info about the data
# titanicData.info()

# adds a new column called pclass and maps it to class. Mapping goes (new column value):(old column value)
titanicData["class"] = titanicData.pclass.map({1: "First", 2: "Second", 3: "Third"})

# prints the first 5 rows of the data
# print(titanicData.head())

# generates the barplot
sns.barplot(titanicData["pclass"], titanicData["survived"])

# shows the barplot
plt.show()
