import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100000)  # another way of generating data
                          # takes in 3 arguments , starting point, ending point
                          # and the number of points in between

y = np.sin(x)             # creating a sine wave

plt.plot(x,y)

plt.xlabel("X-axis")
plt.ylabel("Sine Function")
plt.title("Learning matplotlib")

plt.show()  # we need to actually call the show function to show the plot

