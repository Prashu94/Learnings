# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:20:40 2017

@author: Prashant Prakash Bhat
"""
#Data Anlayis and Wrangling
import pandas as pd
import numpy as np
import random as rnd

#Data Visulazation
import seaborn as sns
import matplotlib.pyplot as plt

#Machine Learning Librarires
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC,LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import GridSearchCV

#Learning curve
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import validation_curve
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import GridSearchCV

#Learning curve
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import validation_curve

import csv
from IPython.display import display

#Loading Train data

PATH = "G:\\extra things\\Knowledge\\Python_Practice\\"

train_df = pd.read_csv(PATH+'train.csv')

#Describing 12 reows of the data
train_df[:12]

#Data Exploration
train_df.info()

#Describing basic statistics of numeric values
train_df.describe()

#Describe objects only

train_df.describe(include = ['O'])

#Finding children under 12
ISChild= train_df.Age.between(0,12)
child12= train_df[ISChild]
display(child12)
child12.info()

#Finding surviced or dead children

child12_dead = child12[child12.Survived == 0]
child12_alive= child12[child12.Survived == 1]

print("Number of children who lived=", child12_alive.PassengerId.count(),
      "\n Number of children who died=", child12_dead.PassengerId.count(),
      "\n Number of all children under the age of 12=",child12.shape[0],
      "\n Percent of survival among under the age of 12 equals",
      round((child12_alive.shape[0]/child12.shape[0])*100,2),"%")

#Check for null
#Cabin 

ISNullCabin = train_df.Cabin.isnull();

#null cabins
nullCabins = train_df[ISNullCabin == True]

nullCabins.describe()

nullCabinsSurvived = nullCabins[nullCabins.Survived == 1]

nullCabinsSurvived.head()
nullCabinsSurvived.info()

#There are 687 passengers with NaN cabins,206 of them survived.

#Features
#correlation matrix

f,ax = plt.subplots(figsize=(12,9))

f
ax
sns.heatmap(train_df.corr(),vmax = .8, square =True)

#Survied correlation with fare and pclass

