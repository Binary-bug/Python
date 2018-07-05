# list_1 = []
#
# list_2 = list()
#
# print("List 1:{}".format(list_1))
#
# print("List 2:{}".format(list_2))
#
# print(list("The lists are equal")


# a list containing two lists
even = [0,2,4,6,8]

odd = [1,3,5,7,9]

numbers=[even,odd]

for numbers_set in numbers:
    print(numbers_set)
    for value in numbers_set:
        print(value)
