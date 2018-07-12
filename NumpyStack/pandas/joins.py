import pandas as pd


# joining different tables together

t1 = pd.read_csv("table1.csv")

t2 = pd.read_csv("table2.csv")


print(t1)

print(t2)

# on is required to join on column 1 , default is row

m = pd.merge(t1,t2,on='user_id')


# method 2
print(t1.merge(t2,on='user_id'))

print(m)

