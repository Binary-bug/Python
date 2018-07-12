#used when we dont know the exact function, e.g. plotting from data

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


A = pd.read_csv("data_1d.csv",header=None).as_matrix()

x = A[:,0] # x axis is the first column colon : means select everything in that
           # dimension

y = A[:,1] # y axis is the second column


plt.scatter(x,y)


# we happened to know what the line that fits this data is

x_line = np.linspace(0,100,100)
y_line = 2*x_line + 1

plt.scatter(x_line,y_line)
plt.show()
