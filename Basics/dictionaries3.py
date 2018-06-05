fruit = {"orange":"a sweet, orange, citrus fruit",
         "apple": " good for making cider",
         "lemon":"a sour, yellow citrus fruit",
         "grape":"a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         "lime":"its yellow"}

print(fruit)

# .items will produce a dynamic view object that looks like tuples
print(fruit.items())

f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + "-" + description)

print("-"*80)

#Python allows to construct dict out of tuples

print(dict(f_tuple))

# strings are actually immutable objects and concatenating two strings in a for loop
# might not be efficient

