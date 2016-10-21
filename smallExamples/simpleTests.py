# some small examples of data visualization
# created by Eric Homberger

# all imports are named by convention
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# dataCreation is a user defined file
import dataCreation as dc

# generates two sets of random data then shows a colored pair plot
def simplePair():
    # We use the randomTrials function in dataCreation which generates some number(in this case 100)
    # of numbers between 0 and some other number (10) and counts the amount of each number
    s1 = dc.randomTrials(10, 100)
    s2 = dc.randomTrials(10, 100)

    # next we combine the two one dimensional series into a dataframe
    df = pd.concat([s1, s2], axis = 1)

    # name the columns and add an index column
    df.columns = ["first", "second"]
    df["index"] = pd.Series(range(10))

    # create a pairplot using the index column to color the points
    sns.pairplot(df, hue = "index")
    plt.show()


# creates an array of points then makes each point the some of all before it and plots the path
def walk():
    # create two 1000 element random arrays
    x = np.random.randn(1000)
    y = np.random.randn(1000)

    # set each element to the sum of itself and every element before it
    x = np.cumsum(x)
    y = np.cumsum(y)

    # plot the x vs the y
    plt.plot(x, y)

    plt.show()


# generates two random Series then creates a dataframe and plots it
def simplePlot():
    # use randomTrials again
    s1 = dc.randomTrials(10, 100)
    s2 = dc.randomTrials(10, 100)

    # create a dictionary based on the results
    d = {'first' : s1,
         'second' : s2,
         'index': range(10)}

    # use the dictionary to create a dataframe then plot it
    df = pd.DataFrame(d)
    plt.plot(df)

    plt.show()
