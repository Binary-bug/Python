import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal as mvn

cov = np.array([[1,0.8],[0.8,3]]) # a covariance matrix

mu = np.array([0,2])

r = mvn.rvs(mean=mu,cov=cov,size=10000)

#plt.scatter(r[:,0],r[:,1])



# using numpy only

r1 = np.random.multivariate_normal(mean=mu,cov=cov,size=10000)

#plt.scatter(r1[:,0],r1[:,1])



# plt.axis('equal')
#
# plt.show()

## other interesting scipy functions

# scipy.io.loadmat # load matlab file , used
#                  #  for data set stored as mat file
#
#
# scipy.io.wavfile.read # open a wav file
#
# scipy.io.wavfile.write # write a wav file

## FFT is in numpy not scipy

x = np.linspace(0,100,10000)

r = np.sin(x) + np.sin(3*x) + np.sin(5*x)

R = np.fft.fft(r) # gives a signal with complex no, should plot magnitude

plt.plot(np.abs(R))

plt.show()
