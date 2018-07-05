for i in range(17):
    print("{0:2} in binary is {0:08b}".format(i))


for i in range(17):
    print("{0:2} in hex is {0:02x}".format(i))

# below is not clear if its decimal or hexadecimal

x = 20

#hence

x=0x20
y=0x0a
print(x)
print(y)
print(x*y)


#specify binary literals using the prefix 0b

print(0b01010)

# leading zeros arent necessary either

print(0b1010)
