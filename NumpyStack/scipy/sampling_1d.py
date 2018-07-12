from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

# we can generate standard normal


#r = np.random.randn(10000)


# to sample from a distribution with arbitrary distribution,
# scale r

r = 10*np.random.randn(10000) + 5 # mean 5 and standard deviation 10


plt.hist(r,bins=100)

plt.show()