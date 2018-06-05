our_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

my_iterator = iter(our_list)

for i in range(0, len(our_list)):
    print(next(my_iterator))

# same implementation

for i in our_list:
    print(i)