#simple example For loops


# range works similar to slicing in strings, the last value in range is not included

# for i in range(1,10):
#     print("i is now {}".format(i))

#
# number = "9,223,372,036,854,775,807"
#
# # for i in range(0,len(number)):  # one of the reasons why range uses one less than the number
# #     print(number[i])
#
# cleanedNumber = ''
#
# for i in range(0, len(number)):  # one of the reasons why range uses one less than the number
#     if(number[i] in '0123456789'):
#         cleanedNumber = cleanedNumber + number[i]
#
# newNumber = int(cleanedNumber)
# print(newNumber)

#Extending for loops

# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''
#
# for char in number:
#     if char in '0123456789':
#         cleanedNumber = cleanedNumber + char
# newnumber = int(cleanedNumber)
# print("The number is {}".format(newnumber))

# for state in ["not pinin'","no more","a stiff","bereft of life"]:
#     print("This parrot is " +state) # alternatively we can use print("The parrot is {}".format(state))
#
# #note range is a sequence type like ["not pinin'","no more","a stiff","bereft of life"] and it actually uses more than just start and end, infact we can use a step
#
# for i in range(0,100,5):
#     print(i)

#nested for loops

# for i in range(1,13):
#     for j in range(1,13):
#         print("{1} times {0} is {2}".format(i,j,i*j),end='\t')
#
#

for i in range(100)[::7]:
    print(i)