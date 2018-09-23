# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 16:59:27 2018

@author: Prashant Bhat
"""

"""
Importing the required libraries
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
##############################################################################
digit_data = load_digits()

"""
Exploring the digits dataset
"""

"""
This is an image dataset containing images of digits like 0 and 1
Image Data Shape- the predictor variables
Lable Data Shape- it gives the lables of the dataset
"""
#Image Data Shape shows there are 1797 images which is 8 by 8 dimension images
print("Image Data Shape:", digit_data.data.shape)
#Image Label Shape are 1797 lables (integers from 0-9)
print("Image Label Shape:", digit_data.target.shape) 

"""
Showing the images an label dataset
1.Write a helper function to plot the image using matplotlib.
"""
def image_label_show(digits,n):    
    plt.figure(figsize = (20,4))
    for index,(image,label) in enumerate(zip(digits.data[0:n],digits.target[0:n])):
        plt.subplot(1,n,index+1)
        plt.imshow(np.reshape(image,(8,8)),cmap=plt.cm.gray)
        plt.title('Training: %i\n' % label, fontsize =20)
image_label_show(digit_data,5)

"""
2. Make a train -test split with 20% of the data set aside for testing. 
Fit a logistic regression model and observe the accuracy.
"""
x_train,x_test,y_train,y_test = train_test_split(digit_data.data,digit_data.target, test_size = 0.20,random_state=0)

"""
Modelling Pattern
1. Import the model you want to use
"""
from sklearn.linear_model import LogisticRegression

"""
2.Make an instance of the model
"""
logistic_regr = LogisticRegression()

"""
3.Training the model of data, storing information learnde from the data
"""
logistic_regr.fit(x_train,y_train)

"""
4.Predict the labels of the new data
Predict for one observation
"""
logistic_regr.predict(x_test[0].reshape(1,-1))

#Predicting for multiple observation at once
logistic_regr.predict(x_test[0:10])

predictions = logistic_regr.predict(x_test)

"""
Measuring Model Performance
"""
score = logistic_regr.score(x_test,y_test)
print(score)

"""
Confusion Matrix
"""
from sklearn import metrics
#Using Seaborm
cm = metrics.confusion_matrix(y_test,predictions)

plt.figure(figsize = (9,9))
sns.heatmap(cm, annot=True,fmt=".3f", linewidths =.5,square=True,cmap='Blues_r')
plt.ylabel('Actual_Label')
plt.xlabel('Predicted_Label')
all_sample_title = 'Accuracy Score: {0}'.format(score)
plt.title(all_sample_title,size=15)
plt.show()

"""
Computing the PCA with 95% of explained variance
"""
from sklearn.decomposition import PCA
#64 is the original
print(x_train.shape)

pca = PCA(0.95)
pca.fit(x_train)
#no components is half which is 28
pca.n_components_

components = pca.transform(x_train)
approximation = pca.inverse_transform(components)

plt.figure(figsize=(8,4))

#Original Image
plt.subplot(1,2,1)
plt.imshow(x_train[0].reshape(8,8),
              cmap = plt.cm.gray, interpolation='nearest',
              clim=(0, 255));
plt.xlabel('64 components',fontsize =14)
plt.ylabel('Original Image',fontsize = 20)

#Principal Components 28
plt.subplot(1,2,2)
plt.imshow(approximation[0].reshape(8,8),
              cmap = plt.cm.gray, interpolation='nearest',
              clim=(0, 255));

plt.xlabel('28 components',fontsize =14)
plt.ylabel('95% Explained variance',fontsize = 20)

###############################################################################

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# Fit on training set only.
scaler.fit(x_train)

# Apply transform to both the training set and the test set.
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)


pca1 = PCA(.95)
pca1.fit(x_train)
pca1.n_components_

x_train_PCA = pca1.transform(x_train)
x_test_PCA = pca1.transform(x_test)

logistic_regr1 = LogisticRegression(solver = 'lbfgs')
logistic_regr1.fit(x_train_PCA,y_train)

logistic_regr1.predict(x_test_PCA[0].reshape(1,-1))

#Predicting for multiple observation at once
logistic_regr.predict(x_test[0:10])

predictions = logistic_regr.predict(x_test)

"""
Measuring the performance
"""
score1 = logistic_regr1.score(x_test_PCA,y_test)
print(score1)

"""
Confusion Matrix
"""
from sklearn import metrics
#Using Seaborm
cm = metrics.confusion_matrix(y_test,predictions)

plt.figure(figsize = (9,9))
sns.heatmap(cm, annot=True,fmt=".3f", linewidths =.5,square=True,cmap='Blues_r')
plt.ylabel('Actual_Label')
plt.xlabel('Predicted_Label')
all_sample_title = 'Accuracy Score: {0}'.format(score1)
plt.title(all_sample_title,size=15)
plt.show()



    
