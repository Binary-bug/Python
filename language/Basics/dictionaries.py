fruit = {"orange":"a sweet, orange, citrus fruit",
         "apple": " good for making cider",
         "lemon":"a sour, yellow citrus fruit",
         "grape":"a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
print(fruit)

print(fruit["lemon"])

print("=="*12)

# another example
# motorbike = {"make":"Honda","model":"250 dream","colour":"red","engine_size":250}
#
# print(motorbike["engine_size"],motorbike["colour"])

fruit["pear"]="an odd shaped apple"
print(fruit)

print("=="*20)
#assigning a value to an existing key, ends up replacing the value

fruit["orange"] = "an orange fruit"
print(fruit)

# reusing a key in a dictionary will result in the same behavior
# as assigning a new value to an existing key i.e.
fruit = {"orange":"a sweet, orange, citrus fruit",
         "apple": " good for making cider",
         "lemon":"a sour, yellow citrus fruit",
         "grape":"a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         "lime":"its yellow"}

#look how lime is repeated twice in the above definition

print(fruit)

# removing items from a collection

print("=="*20)

del fruit["orange"]
print(fruit)

#if you forget to specify the key-value pair to delete
# it deletes the entire dictionary

## del fruit
## print(fruit) will throw an error

# if you want to empty out the dictionary do this

#fruit.clear()
#print(fruit)

# trying to retrieve an item that doesn't exit will result in a
# KeyError
## print(fruit["orange"])

# Accessing dictionary values on the fly, invalid keys return None from .get()


while True:
    dict_key = input("Please input the key: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        key_value = fruit.get(dict_key)
        print(key_value)
    else:
        print("we dont have that " + dict_key)

