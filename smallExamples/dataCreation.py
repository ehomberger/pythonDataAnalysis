#This file will contain a few functions designed to give different data distributions
import numpy as np
import pandas as pd


#randomly assign a value to each element in a series
def randomDist(elements):
    s = pd.Series(np.random.randn(elements))
    return s

#generate 'trials' random numbers between 0 and 'elements' then return a series based on frequency
def randomTrials(elements, trials):
    #generate the random integers
    data = np.random.randint(low = 0, high = elements, size = trials)

    #create a list based of the data so we can use .count() then use list comprehension to generate frequencies    
    l = list(data)
    counts = [l.count(x) for x in range(elements)] 

    #turn the data into a series and return it
    s = pd.Series(counts, range(elements)) 
    return s
