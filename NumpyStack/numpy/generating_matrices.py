import numpy as np

#naively

A = np.array([1,2,3])

print(A)

#creating an 1D array of all zeros, note matrices are nothing but
# 2D arrays

A = np.zeros(100)  # pass the size of the array to get a vector of all zeros

print(A)


# matrix of size 5x10 with all zeros

A = np.zeros((5,10))

print(A)

#equivalent function to create all ones

A = np.ones(10)
print(A)

A = np.ones((7,10))
print(A)

# for random values inside the matrix

A = np.random.random((4,4))
print(A)

# notice that the above random numbers generated lie in the range(0,1)
# The Probability distribution the random numbers came from are an
# interesting aspect

## np.random.random gives us uniformly distributed random numbers from 0 to 1

# for Gaussian distrbution we use randn, notice the function call

G = np.random.randn(4,4)  ## randn takes takes each of the dimension in arguments not in
## not in tuples

print(G) # these numbers are from a gaussian distribution with mean zero
# and variance 1


# numpy array also has convenient functions to calculate the statistics
# like mean

print(A.mean())
print(A.var())

print(G.mean())
print(G.var())
