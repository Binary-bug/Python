# to check what are imported automatically use this

print(dir())

# anything with an underscore is private to that module and should nt be changed
# though, it is not enforced


# double underscore should never changed.

# __builtins__

#print(dir(__builtins__))

for m in dir(__builtins__):
    print(m)


print('*'*40)

import shelve

print(dir(shelve))



#notice that close isnt present since close is part of the shelf object


for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print(obj)




#using help with python

help(shelve) # help can be called on functions too

import random

help(random.randint)