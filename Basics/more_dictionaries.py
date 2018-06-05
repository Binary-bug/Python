# two more methods on dictionaries , update and copy

fruit = {"orange":"a sweet, orange, citrus fruit",
         "apple": " good for making cider",
         "lemon":"a sour, yellow citrus fruit",
         "grape":"a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         "lime":"its yellow"}

print(fruit)

veggie = {"cabbage":"every childs favorite",
          "sprouts":"mmmmmmmm, lovely",
          "spinach":"Can i have some more fruit please"}

print(veggie)

veggie.update(fruit) # .update method return vlaue is None

#In order to create a new dictionary that will contain all the items from the
#above dictionary, instead of using update use copy

temp = fruit.copy()

temp.update(veggie)

print(temp)

