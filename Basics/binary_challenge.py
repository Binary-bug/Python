decimal =  int(input("Please enter an non-negative integer less than 65535"))
binary=0
while decimal//2:
    if decimal % 2:
    binary += (decimal % 2) * 10
    decimal = decimal // 2
print(binary)


#Tim's answer
# powers =[]
#
# for power in range(15,-1,-1):
#     powers.append(2 ** power)
#
# print(powers)
# x = int(input("Please enter a number:"))
#
# for power in powers:
#     print(x // power, end='')
#     x %=power
#octal variant
