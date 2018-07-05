import numpy as np

A = np.array([[1,1],[1.5,4]])

b = np.array([2200,5050])

popul = np.linalg.solve(A,b)

print("The number of children and adults are {} , {}".format(int(popul[0]),int(popul[1])))