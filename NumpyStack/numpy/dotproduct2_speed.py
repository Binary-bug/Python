import datetime
import numpy as np

a = np.random.randn(100) # creates a random numpy array of 100 elements

b = np.random.randn(100)

T = 100000

def slow_dotproduct(a,b):
    result = 0
    for e,f in zip(a,b):
        result += e*f
    return result


t0 = datetime.datetime.now()
for x in range(T):
    slow_dotproduct(a,b)
t1 = datetime.datetime.now()



t2=datetime.datetime.now()
for x in range(T):
    a.dot(b)
t3=datetime.datetime.now()

print("ratio between times are {}".format(1/((t3-t2).total_seconds()/(t1-t0).total_seconds())))