import numpy as np


x = []

for line in open("data_2d.csv"):
    row = line.rsplit(',')
    sample = list(map(float,row))  # cast these string values into float
    x.append(sample)

#
# for row in x:
#     print(list(row)) # since x is a list of lists we can convert it into
#                      # a numpy array

x = np.array(x)

print(x)