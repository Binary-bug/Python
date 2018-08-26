__author__='Sarat Chandra B, SRNO: 14848'
from PIL import Image
import os
import numpy as np
from pylab import *
from natsort import natsorted, ns
import re
from sklearn.neighbors import NearestNeighbors as nn



def natural_sort( l ):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    l.sort( key=alphanum_key )

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
        tmp *= 1/(column-1)
        eigen_faces = tmp[::-1]
        S = []
        for i in eigen_faces[:]:
            S.append(np.linalg.norm(i))
        # S = np.sqrt(eigen_values)[::-1]
        for i in range(eigen_faces.shape[1]):
             eigen_faces[:,i] /= S
    else:
        dummy, eigen_values, eigen_faces = np.linalg.svd(X)
        eigen_faces = eigen_faces[:row]


    return eigen_faces,eigen_values,empirical_mean





current_path, __ , __ = next(os.walk(os.getcwd()))

traindata_path = current_path + "/training_data/"
testdata_path = current_path + "/test_data/"

training_data = os.listdir(traindata_path)
test_data = os.listdir(testdata_path)



train_list = [filename for filename in training_data if filename[-4:] in [".pgm"]]
test_list = [filename for filename in test_data if filename[-4:] in [".pgm"]]

natural_sort(train_list)
natural_sort(test_list)

raw_matrix = np.asarray([np.array(Image.open(traindata_path+im)).flatten() for im in train_list],'f')
test_matrix = np.asarray([np.array(Image.open(testdata_path+im)).flatten() for im in test_list],'f')

im = array(Image.open(traindata_path+ train_list[0]))
m,n = im.shape

Eigen_faces,Eigen_values,Empirical_mean = pca(raw_matrix)


#Step 2.5: Choosing the value of K
Eigen_total = np.sum(Eigen_values)
K = np.argmin(Eigen_values.cumsum() < (0.95 * Eigen_total))



#Step 3: Take some random image from the training set and compute K coefficients
random_train_image = np.array(Image.open(traindata_path+train_list[np.random.randint(0,len(train_list))])).flatten()
coeff_train = np.dot(random_train_image,np.transpose(Eigen_faces[:K]))


#Step 4: Reconstruction of the sample image and original
reconstructed_train_image = np.dot(coeff_train,Eigen_faces[:K]) + Empirical_mean

figure(1)
gray()
subplot(2,4,1)
imshow(random_train_image.reshape(m,n))
subplot(2,4,2)
imshow(reconstructed_train_image.reshape(m,n))

savefig("Reconstruct_TrainImage_K_{}.png".format(K), format='png', dpi=300)

#Step5: Classification of test samples in the eigen space
classification_count = 0

#construction of K-coefficients of each image in the training set
Kcoeff_train = []
for i in raw_matrix:
    Kcoeff_train.append(np.dot(i,np.transpose(Eigen_faces[:K])))

Kcoeff_test = []
for i in test_matrix:
    Kcoeff_test.append(np.dot(i, np.transpose(Eigen_faces[:K])))

Kcoeff_test = array(Kcoeff_test)
Kcoeff_train = array(Kcoeff_train)

for i in range(Kcoeff_test.shape[0]):
    neigh = nn(n_neighbors=1)
    neigh.fit(Kcoeff_train)
    classification_index = neigh.kneighbors(Kcoeff_test[i].reshape(1,-1))[1]
    if classification_index // 8 == i // 2:
        classification_count += 1

percentage_of_error = (Kcoeff_test.shape[0] - classification_count) / classification_count
print("Classification Error over test sample is {}".format(100*percentage_of_error))


#Step7: Take some random image from test set and comput K coefficients
random_test_image = np.array(Image.open(testdata_path+test_list[np.random.randint(0,len(test_list))])).flatten()
coeff_test = np.dot(random_test_image,np.transpose(Eigen_faces[:K]))

#Step 7.5: Reconstruction of the sample image and original
reconstructed_test_image = np.dot(coeff_test,Eigen_faces[:K]) + Empirical_mean

figure(2)
gray()
subplot(2,4,1)
imshow(random_test_image.reshape(m,n))
subplot(2,4,2)
imshow(reconstructed_test_image.reshape(m,n))
savefig("Reconstruct_TestImage_K_{}.png".format(K), format='png', dpi=300)

