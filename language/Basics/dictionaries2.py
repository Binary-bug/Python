fruit = {"orange":"a sweet, orange, citrus fruit",
         "apple": " good for making cider",
         "lemon":"a sour, yellow citrus fruit",
         "grape":"a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         "lime":"its yellow"}

print(fruit)

while False:
    dict_key = input("Please input the key: ")
    if dict_key == "quit":
        break
    #Alternative to this below commented code
    # if dict_key in fruit:
    #     key_value = fruit.get(dict_key)
    #     print(key_value)
    key_value=fruit.get(dict_key,"we dont have that value " + dict_key)
    print(key_value)

# iterate over the keys
#for fruits in fruit:
#    print(fruit[fruits])

# ordering the list of keys
#ordered_key = list(fruit.keys())
#ordered_key.sort()

#alternatively
# ordered_key = sorted(list(fruit.keys())
#for f in ordered_key:
#    print(f + '-' + fruit[f])

# alternative for the for loop above

#for f in sorted(fruit.keys()):
#    print(f + '-' + fruit[f])

#fruit.keys doesnt return a list, but it behaves as a sequence

# values command to get the values though less efficient than using the keys
# like in the above code

for val in fruit.values():
    print(val)
print("=====================")

print(fruit.keys())
print(fruit.values())


fruit_keys = fruit.keys()
print(fruit_keys)

fruit["tomato"]="not ice with an icecream"

print(fruit_keys)













