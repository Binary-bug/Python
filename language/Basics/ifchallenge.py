name = input("Please enter your name and age")
age = int(input())

if 17 < age < 32:
    print("Welcome to the holiday {}".format(name))
else:
    print("Sorry {}, you are not old enough. Please come back in {} years".format(name,18 - age))