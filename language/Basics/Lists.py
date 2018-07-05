# ipAddress = input("Please input and ip address")
# print(ipAddress.count('.'))

# parrot_list = ['not pinin\'','no more','a stiff','bereft of life']
#
# parrot_list.append('A Norwegian Blue')
# for state in parrot_list:
#     print("This parrot is "+ state)

even = [0,2,4,6,8]

odd =[1,3,5,7,9]

numbers = even + odd
#numbers.sort()
#print(numbers)
numbers_in_order=sorted(numbers)
print(numbers_in_order)

if numbers == numbers_in_order:
    print("The lists are equal")
elif numbers_in_order==sorted(numbers):
    print("They contain same items")
else:
    print('the lists are not equal')
