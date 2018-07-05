import numpy as np

L = [1,2,3]

A = np.array([1,2,3])

for e in L:
    print(e)

for e in A:
    print(e)


L.append(4) # there is no append method to add element to array
print(L)

L += [5]  # even this wont work with array A
print(L)

# Vector Addition L + L

L2 = []

for e in L:
    L2.append(e+e)

print(L2)

#Vector Addition with array as simple as that without a loop
# + sign with numpy arrays does vector addition
# if A was a matrix , it would do 2D addition i.e. element wise addition

A += A
print(A)

#scalar multiplication

A *= 2
print(A)

A //= 2

print(A)

# raise to the power

print(A**2)


# element wise square root

print(np.sqrt(A))

# element wise log

print(np.log(A))

#element wise exponential

print(np.exp(A))