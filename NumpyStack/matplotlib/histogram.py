# histogram is nothing but a discretized probability distribution of the
# data


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


A = pd.read_csv("data_1d.csv",header=None).as_matrix()

x = A[:,0] # x axis is the first column colon : means select everything in that
           # dimension

y = A[:,1] # y axis is the second column


#plt.hist(x)

# random.random gives uniform distribution

#r = np.random.random(10000)

#plt.hist(r)

# we can control the number of buckets ,default is ~ 10

#plt.hist(r,bins=20)

# errors are normally distributed

y_actual = 2*x+1

residuals = y - y_actual

plt.hist(residuals)

plt.show()