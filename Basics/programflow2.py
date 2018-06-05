# age = int(input("How old are you"))
#
# # if age >= 16 and age <= 65:
# #     print("Have a good day at work")
# #
# # # age has a lower priority than conditional operators
# #
# #
# # # alternate way to write the above piece of code
#
# # if 15 < age < 66:
# #     print("Have a good day at work")
# #
#
#
# if ( age < 16) or (age > 65):
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")


# # x = "false"
#
# if x:
#     print("x is true")


# NOTES
#
# 1) its possible to create a class that evaluates to false
# 2) In Python, evey non-zero value is evaluated to false.

# x = input("please enter some text")
# if x:
#     print("YOu entered '{}'".format(x))
# else:
#     print("YOu did not enter anything")

# code that uses not true is equal to false and vice-versa i.e. not is a keyword here
#
# print(not True)
#
# print(not False)

#KEYWORD not
# age = int(input("How old are you"))
# if not(age < 18):
#     print('YOu are old enough to vote')
#     print("please put your vote in the ballot")
# else:
#     print("Please come back in {} years ".format(18 - age))
#
# #KEYWORD in

parrot = "Norwegian Blue"

letter = input("Enter a character")

if letter in parrot:
    print("Give me an {},Bob".format(letter))
else:
    print("I don't need that letter")

#alternate to the above piece of code

parrot = "Norwegian Blue"

letter = input("Enter a character")

if letter not in parrot:
    print("I don't need that letter")
else:
    print("Give ma an {},Bob".format(letter))
