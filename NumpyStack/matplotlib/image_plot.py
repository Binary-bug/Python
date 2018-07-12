import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("train.csv")

print(df.shape)

M = df.as_matrix()

# the goal is to display an image

#selecting the first image

img1 = M[0,1:] # since all the pixels in an image is vectorized into a row

# converting it back to image

img1 = img1.reshape(28,28)

#plt.imshow(img1)

#setting  the colormap

plt.imshow(img1,cmap='gray') # black corresponds to a pixel value of 0
                             # white corresponds to a pixel value of 255

#invert the colos

plt.imshow(255-img1,cmap='gray')
plt.show()