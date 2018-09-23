# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 18:28:44 2018

@author: Prashant Bhat
"""
"""
Import the required packages
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
##############################################################################
"""
Load the data
"""
path = "G:\\extra things\\Knowledge\\practice\\Edureka\\Module9\\"
data_v = pd.read_csv(path+"voice-classification.csv")

"""
Exploring data
"""

data_v.columns
"""
We check for object type column, and label is the only one which is the object type 
"""
data_v.info()

"""
Now we want to the distinct groups in the voice data for labels attribute
"""
data_v.groupby('label').groups.keys()

"""
We now remove the other columns which are not required from the data_v dataframe
Visualizing the correlation metric for the above datset to check which attribute can be removed or inconsequential
"""

corr_matrix =  data_v.corr()
print(corr_matrix)

sns.heatmap(corr_matrix,square = True,cmap= plt.cm.RdYlGn)
plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.show()

X,y = data_v.iloc[:,[1,3,4,5,7,8,9,10,12,13,15,16,18]].values,data_v.iloc[:,-1].values

"""
Preprocessing the y varible for fitting the model
"""
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=1)


"""
Building a model- naive bayes
"""
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
y_pred_gnb = gnb.fit(x_train,y_train).predict(x_test)


"""
Creating a confusion matrix
"""
from sklearn.metrics import confusion_matrix
cnf_matrix_gnb = confusion_matrix(y_test,y_pred_gnb)
print(cnf_matrix_gnb)

from sklearn import metrics
print(metrics.accuracy_score(y_pred_gnb,y_test))





