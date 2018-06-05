# farm_animals = {"sheep","cow","hen"}
#
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("="*40)
#
# wild_animals = set(["lion","tiger","panther","elephant","fox"])
#
# print(wild_animals)
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
#
# print(farm_animals)
# print(wild_animals)
#
# #creating an empty set as empty_set={} would return a dictionary
#
#
# empty_set = set()
# empty_set2 = {}
#
# empty_set.add("a")
# #empty_set2.add("a") will throw an error saying that no add attribute to the dict object
#
# #an iterative object can be passed as arguments to the set function
# #though we used lists in the above code, we can also use ranges, tuples
#
#
# even = range(0,40,2)
# even_set = set(even)
# print(even_set)
#
# squares_tuple = (4,9,6,16,25)
#
# print(set(squares_tuple))
#
#Union , intersection, difference and subsets of Sets

even = set(range(0,40,2))
print(even)
print(len(even))

squares = set((4,9,6,16,25))
print(squares)
print(len(squares))

#union syntax

print(even.union(squares))
print(len(even.union(squares)))
#or
print(squares.union(even))

#intersection
print(even.intersection((squares)))

#or

print(squares.intersection((even)))

# alternatively and can be used

print(squares & even)


# to implement set A \ set B

print("="*100)

print(sorted(even))
print(sorted(squares))
#two methods to find the difference
print(sorted(even.difference(squares)))
print(sorted(squares.difference(even)))
print(sorted(squares - even))
print(sorted(even - squares))

print("="*40)

# difference_update method changes the even set in place
#print(sorted(even))
#even.difference_update(squares)
#print(sorted(even))

# print("symmetric difference")
# symmetric difference is nothing but elements which are in either one set or the other but not both
# print(sorted(even.symmetric_difference(squares)))
#
# print(sorted(squares.symmetric_difference(even)))

# Similar to difference_update symmetric_difference_update behaves likewise, but its just that
# it performs symmetric difference

# There are two methods to perform remove operation from sets which are discard and remove
# Remove raises an error if the item to be removed doesnt exit
# Discard wont actually raise an error

squares.discard(4)
squares.remove(16)
squares.discard(8)
print(squares)

# try catch to raise an exception to handle errors

try:
    squares.remove(8)
except KeyError:
    print("the item 8 is not a member of the set")

# Subset and Superset
print("="*40)

even = set(range(0,40,2))
print(even)
squares_tuple = (4,6,16)
squares = set(squares_tuple)
print(squares)

if squares.issubset(even):
    print("squares is a subset of even")
if even.issuperset(squares):
    print("even is a superset of squares")

# Another type of set called frozen set whose items cannot be changed i.e. immutable

#frozen set
print("="*40)
even = frozenset(range(0,100,2))
print(even)



