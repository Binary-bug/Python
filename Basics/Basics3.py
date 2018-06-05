# greeting = "Bruce"
# _myName = "Tim"
# Time45 = " Good"
# Time_was_57 = "Hello"
# Greeting = "There"
#
# print(Time_was_57 + ' ' + greeting)
#
# age = 24
#
# print(age)
#
# print(greeting + str(age))
#


#Basic Data types

a = 13
b = 3
print(a + b)
print(a - b)
print(a*b)
print(a/b) #division in python by default uses float
print(a // b) # to do integer divison use doubleslash
print(a%b)


#use case for integer divison

for i in range(1,a//b):
    print(i)

#in the above piece of code, you can have a /b since its a float and cannot be used with for in range


#String Data types

parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
print(parrot[-1])

print(parrot[:6])

print(parrot[6:])

print(parrot[-4:2]) #doesnt work because -4 is the 4th character from last and you cant go backwards here but
#this would work

print(parrot[-4:-2])

#additional tricks

print(parrot[0:6:2]) # meaning print from index 0 upto 6 in steps of 2

#useless application

number="9,223,372,036,854,775,807"
print(number[1::4]) # meaning print from index 1 upto the last character in steps of 4

#better example

numbers = "1,2,3,4,5,6,7,8,9"
print(numbers[0::2])


#More on String operators

string1 = "he's "
string2 = "probably "
print(string1 + string2)
print("he's " " probably " "pining" ) #concatenate alternate

#multiply strings

print("Hello" * 5)

#erroneous code due to operator precedence print("Hello" * 5 + 4)


#if you wanted to append 4 to the string you could use like this

print("hello " *5 + "4")

#search for a substring
today="friday"

print("day" in today) # in is an operator here

print("fri" in today)

print("Thursday" in today)

print("fridays" in today)




