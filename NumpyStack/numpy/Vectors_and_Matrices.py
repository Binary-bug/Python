# a Matrix is a two dimensional array or a list of lists
import numpy as np

M = np.array([[1,2],[3,4]])


#convention is the 1st index is the row and second index is the column

print(M[0])

# list of lists

L = [[1,2] , [3,4]]

print(L[0])


#to access access a specific element say 3 , we have

print(L[1][0])

#with numpy array we get

print(M[1][0])

# shorthand notation which is natural for matrices

print(M[1,0])


##NOTE##

## there is an actual data type in numpy called matrix

''' its used as numpy.matrix'''


M2 = np.matrix([[1,2],[3,4]]) # works similar to the numpy array

print(M2)

# official numpy documentation recommends against using numpy array
# so if you see a matrix convert it to array like this

M2 = np.array(M2)


#even though its an array we have convenient matrix operations

# to get the transpose

print(M2.transpose())

#or

print(np.transpose(M2))

#or

print(M2.T)  #calling transpose

