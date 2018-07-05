import numpy as np

# solving a Linear system Ax=b

# if A is invertible , then x is unique

A = np.array([[1,2],[3,4]])

b = np.array([1,2])

# the solution to this is,
x = np.linalg.inv(A).dot(b)
print(x)

# since this is such a common operation in numpy, there is a better way
# to do it

y = np.linalg.solve(A,b) # inverse method is too computationally expensive
print(y)

