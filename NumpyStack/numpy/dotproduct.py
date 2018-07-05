import numpy as np


a = np.array([1, 2])

b = np.array([2, 1])

#naive dot product

# dot = 0
#
# for e,f in zip(a,b): # zip groups and packs into 1 single list
#     dot += e*f

dot = a*b  # multiplies element wise so cant be done with different sizes
print(dot)

#now to get dot product from above implementation sum all the terms in dot

print(np.sum(dot)) # sum method is an instance method of the numpy array
                   # itself
#so alternatively
print(dot.sum())

#though both the above methods give the answer , more convenient way to
#calculate the dot product

print(np.dot(a,b))

#like the sum function, the dot function is also an instance method

print(a.dot(b)) # so we can directly call on the array object itself

#or
print(b.dot(a))

## Calculate the angle between a and b using alternate definition of
## dot product

result = a.dot(b) / (np.sqrt((a**2).sum()) * np.sqrt((b**2).sum()))

print(result)
angle = np.arccos(result) # angle between the vectors default in radians

print(angle)

# alternatively we can find it by using

result = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))

print(result)

print(np.arccos(result))




