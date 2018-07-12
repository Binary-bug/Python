import numpy as np
import matplotlib.pyplot as plt


r = np.random.randn(10000,2)



# elliptical gaussian where variance is different for each gaussian

r[:,1] = 5*r[:,1] + 2

plt.scatter(r[:,0],r[:,1])

plt.axis('equal') # since matplot lib scales 
plt.show()