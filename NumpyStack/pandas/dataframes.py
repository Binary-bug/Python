import pandas as pd

x = pd.read_csv("data_2d.csv",header=None) # pandas style loading data

print(type(x)) # returns a pandas Data frame

# data frames have quite useful functions

# info function

print(x.info())

# head function gives a preview of whats inside the data frame

print('*'*40)

print(x.head()) # specifically prints out the first few rows
                # if you want a specific number of rows, just pass it to
                # the head function

print(x.head(10))


# do Dataframes act like 2D numpy arrays?? NO

# method 1 : Convert the dataframe into numpyarray

M = x.as_matrix()

print(type(M))

# working with data frames

print(x[0]) # fetches the first column

# clear distinction

# with numpy array  x[0] fetches the first row
# wherein in pandas x[0] fetches the column with name 0

print(type(x[0])) # returns a pandas Series object

# pandas data frames are for 2D objects whereas pandas series are for 1D
# objects

# Fetching rows with dataframes

#method1:

print(x.iloc[0])

#method2:

print(x.ix[0])  # both are series objects

# Selecting multiple column at a time

print(x[[0,2]])  # fetches the first and third column

# selecting rows that satisfy a criterion

print(x[x[0] < 5])  # fetches rows in the 0th column that are less than 5

print(x[0] < 5)  # the arguments above mean passing a 1D object of boolean
                 # and its a series object





