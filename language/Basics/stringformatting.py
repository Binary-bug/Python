age = 24

print("My age is " + str(age) + " years ")


# the above procedure is tedious since we dont really want to include str for every number we encounter

#Method1 Replacement Fields

print("My age is {0} years ".format(age)) # {0} is the actual replacement field, number important for multiple replacement fields

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} ".format(31,"January","March","May","july","August","october","december"))

#each of the arguments of .format are matched to their respective replacement fields

print("""January:{2}
February:{0}
March:{2}
April:{1}
""".format(28,30,31))

#Method2 Formatting operator not recommended though style from python 2


print("My age is %d years" % age)
print("My age is %d %s, %d %s" % (age,"years",6,"months"))

#^ old format and it was elegant -__-

#
# for i in range(1,12):
#     print("No, %2d squared is %4d and cubed is %4d" %(i,i**2,i**3)) # ** operator raises power %xd x allocates spaces
#
#
#
#
# #for comparison
# print()
# for i in range(1,12):
#     print("No, %d squared is %d and cubed is %d" % (i,i**2,i**3))
#
#
# #adding more precision
#
# print("Pi is approximately %12.50f" % (22/7)) # 50 decimal precsion and 12 for spaces default is 6 spaces
#
#
#
#

#Replacement field syntax variant of above Python 2 tricks

for i in range(1,12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i,i**2,i**3))

print()
#for left alignment

for i in range(1,12):
    print("NO. {0:<2} squared is {1:<4} and cubed is {2:<4}".format(i,i**2,i**3))


#floating point precision
print("Pi is approximately {0:.50}".format(22/7))

#use of numbers in replacement fields is optional when the default order is implied

for i in range(1,12):
    print("No. {:2} squared is {:4} and cubed is {:4}".format(i,i**2,i**3))

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])