# international airline passengers .csv , column names are ugly

# end of the file unnecessary comments have to be removed

import pandas as pd
import datetime

def get_interaction(row):
    return row['month']*row['passengers']


df = pd.read_csv("international-airline-passengers.csv",engine="python",skipfooter=3)

# skipfooter rows will skip the bottom 3 rows

# skipfooter doesnt work with the default engine, hence using engine python

# check column names , they are kinda ugly though

print(df.columns)

# reassigning column names by passing it a list

df.columns = ['month','passengers']

print(df.columns)

# selecting a column

#method1

print(df['month'])

# when column names are strings ,we can use this method

print(df.month)
print(df.passengers) # this wouldnt have worked if column names had space
                     # hence we reassigned the column names

# adding a new column

df['ones'] = 1 # will add a column of 1's

print(df.head()) # to add a column of different values we use apply function


# apply function
### to apply a new column value based on the other data
# in the row


#df['month*passengers'] = df.apply(lambda row:row['month']*row['passengers'],axis=1)

# axis = 1 is necessary for the function to be applied across each row

# if you are not familiar with lambda , define  a function

#df['month * passengers'] = df.apply(get_interaction,axis=1)

#example

df['dt'] = df.apply(lambda row: datetime.datetime.strptime(row['month'],'%Y-%m'),axis=1)

print(df.info())