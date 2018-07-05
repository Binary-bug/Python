import numpy as np


A = np.array([[1,2],[3,4]])

# matrix inverse, the inverse function is in the linalg module


a_inv = np.linalg.inv(A)
print(a_inv)

# verifying the Inverse by multiplying with A resulting in I

print(a_inv.dot(A))

# matrix determinant

det_a = np.linalg.det(A)
print(det_a)

# diagonal of a matrix

diag_a = np.diagonal(A) # gives diagonal elements in a vector
print(diag_a)

# to make a 2D array of diagonal

diag_2d = np.diag(diag_a)
print(diag_2d)

# remember that if you pass a 2D array to diag it will
# return diagonal elements in a 1D array

## if you pass a 1D array to diag, it will return a 2D array where the
## off diagonals are zero and the original array takes up the diagonal

#Outer Product

a = np.array([1,2])

b = np.array([3,4])

out_prod = np.outer(a,b)
print(out_prod)

# we can also do inner product like below, inner product is the same
# as outer product

inn_prod = np.inner(a,b)
print(inn_prod)

# Trace of a Matrix , is nothing but the sum of the elements of diagonal

#method1
print(A)
print(np.diag(A).sum())

#method2
print(np.trace(A))


x = np.random.randn(100,3) # by convention this is 100 observations
                           # 3 features
#to calculate covariance
cov = np.cov(x)
print(cov)

print(cov.shape) # this results in (100,100) which is wrong
                 # since we have only 3 features , it has to be (3,3)


print(np.cov(np.transpose(x)).shape) # this looks ugly

# there are two methods to calculate eigenvalues and eigenvectors

# np.eig(A) and np.eigh(A) ; eigh is used for symmetric matrices
# and hermitian matrices

# symmetric means a == transpose(a)

# hermitian means a == conjugate transpose ( a )

# since covariance is a symmetric matrix , we are using eigh

eig_cov = np.linalg.eigh(cov) # gives out a tuple containing
                              # in the first eigenvalues
                              # in the second corresponding eigenvectors
print(eig_cov)







