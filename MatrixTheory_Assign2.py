from PIL import Image
import os
import numpy as np
from pylab import *


def pca(R):

    #get dimensions
    row, column = R.shape

    # center data
    empirical_mean = R.mean(axis=0)
    X = R - empirical_mean

    if column > row:
        X_T = np.transpose(X)

        M = np.dot(X,X_T)
        eigen_values, eigen_vectors = np.linalg.eigh(M)

        tmp = np.transpose(np.dot(X_T, eigen_vectors))

        eigen_faces = tmp[::-1]
        S = []
        for i in eigen_faces[:]:
            S.append(np.linalg.norm(i))
        #S = np.sqrt(eigen_values)[::-1]
        for i in range(eigen_faces.shape[1]):
             eigen_faces[:,i] /= S
    else:
        dummy, eigen_values, eigen_faces = np.linalg.svd(X)


    return eigen_faces,eigen_values,empirical_mean




training_data = "training_data"

test_data = "test_data"


allfiles = os.listdir(os.getcwd())

train_list = [filename for filename in allfiles if filename[-4:] in [".pgm"]]

raw_matrix = np.asarray([np.array(Image.open(im)).flatten() for im in train_list],'f')

im = array(Image.open(train_list[0]))
m,n = im.shape

Eigen_faces,Eigen_values,Empirical_mean = pca(raw_matrix)


#Step 2.5: Choosing the value of K
Eigen_total = np.sum(Eigen_values)
K = np.argmin(Eigen_values.cumsum() < (0.95 * Eigen_total))



#Step 3: Take some random image from the training set and compute K coefficients
random_image = np.array(Image.open(train_list[np.random.randint(0,len(train_list))])).flatten()
coeff = []
for i in range(K):
      coeff.append(np.dot(random_image,Eigen_faces[i]))

print(coeff)
#Step 4: Reconstruction of the sample image and original
reconstructed_image= np.dot(coeff,Eigen_faces[:K])


figure()
gray()
subplot(2,4,1)
imshow(random_image.reshape(m,n))
subplot(2,4,2)
imshow(reconstructed_image.reshape(m,n))

show()
