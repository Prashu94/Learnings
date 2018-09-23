# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 16:44:54 2018

@author: Prashant Bhat
"""

"""
Loading the Required libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
##############################################################################


"""
Loading the voices.csv data file
"""

path = "G:\\extra things\\Knowledge\\practice\\Edureka\\Module7\\"
data = pd.read_csv(path+"voice.csv")
print(list(data.columns))
data.head(1)

##############################################################################
"""
Identifying the depenedent and independent variable
label is the dependent variable
and others are independent variables
"""

#Data Manipulation
sns.countplot(data['label'],label = "counts")


le = preprocessing.LabelEncoder()
le.fit(data['label'])
le.classes_
data['label_encoded']=le.transform(data['label'])

pred_columns = data[:]
pred_columns.drop(['Q25'],axis=1,inplace = True)
pred_columns.drop(['Q75'],axis=1,inplace = True)
pred_columns.drop(['IQR'],axis=1,inplace = True)
pred_columns.drop(['label'],axis=1,inplace=True)
prediction_var = pred_columns.columns
print(list(prediction_var))

#Train Test Split

train,test = train_test_split(data,test_size = 0.3)
print(train.shape)
print(test.shape)

train_X = train[prediction_var]
train_Y = train['label_encoded']

test_X = test[prediction_var]
test_Y = test['label_encoded']

#Model Creation

logistic = LogisticRegression()
model = logistic.fit(train_X,train_Y)

#Prediction

temp = logistic.predict(test_X)

#Accuracy

print(metrics.accuracy_score(temp,test_Y))

"""
3. Compute the correlation matrix that describes the dependence between all predictors and identify the predictors that are highly correlated. 
Plot the correlation matrix using seaborn
"""
sns.heatmap(data)

"""
4. Based on correlation remove those predictors that are correlated and fit a logistic regression model again and compare the accuracy with that of previous model.
"""

sns.heatmap(data[prediction_var])

