# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 23:05:49 2018

@author: Prashant Bhat
"""

"""
Import the required datasets
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
###############################################################################
"""
Loading the dataset breast-cancer data
"""
path = "G:\\extra things\\Knowledge\\practice\\Edureka\\Module8\\"
data_b = pd.read_csv(path+"breast-cancer-data.csv")

"""
Exploring the loaded data
"""
#print the column names
data_b.columns
data_b.head(1)
data_b.dtypes
null_columns = dict(data_b.isnull().any()[lambda x:x])

data_b.groupby('diagnosis').groups.keys()

print(data_b.shape)

X = data_b.drop('diagnosis',axis=1)
y = data_b['diagnosis']

x_train,x_test,y_train,y_test = train_test_split(X,y,test_size =0.20,random_state =0)

pca =PCA(n_components=2)
pca.fit(x_train)
pca.n_components_

x_train_PCA = pca.transform(x_train)
x_test_PCA = pca.transform(x_test)

from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()
dtree.fit(x_train_PCA,y_train)

predictions = dtree.predict(x_test_PCA)

df_bc = pd.DataFrame(predictions,y_test)
print(df_bc)
#82% accuracy
score1 = dtree.score(x_test_PCA,y_test)
print(score1)

from sklearn.metrics import classification_report,confusion_matrix

print(classification_report(y_test,predictions))

print(confusion_matrix(y_test,predictions))

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
