import numpy as np
from scipy.stats import norm

print(norm.pdf(0))  # probability distribution for 0 from standard normal

print(norm.pdf(0,loc=5 , scale=10)) # guassian of 0 with mean 5 , std deviation 10

# multiple values at the same time , no need of for loop


r = np.random.randn(10)

print("value of r is {}".format(r))

print(norm.pdf(r))

# commonly we use log of pdf function

print(norm.logpdf(r))

## cdf or cumulative distribution function

print(norm.cdf(r))

print(norm.logcdf(r))