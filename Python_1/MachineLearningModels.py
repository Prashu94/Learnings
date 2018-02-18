# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 13:52:37 2018

@author: user
"""

import csv

import pandas as pd

"""
Loading and Preprocessing
"""
PATH = "G:\\extra things\\Knowledge\\Python_Practice\\"

train_df = pd.read_csv(PATH+'train.csv',index_col = 'PassengerId') 
test_df = pd.read_csv(PATH+'test.csv',index_col = 'PassengerId')

train_df.describe()
test_df.describe()

"""
Pre-Processing
combine train/test data to simulatneously apply transformations
"""

Survived = train_df['Survived'].copy()
train_df = train_df.drop('Survived',axis=1).copy()

df = pd.concat([train_df,test_df])

df.describe()
df.info()

traindex = train_df.index
testdex = test_df.index

#removes the object from the memeory
del train_df
del test_df    

"""
To understand Feature Engineering
"""
#Feature Engineering

full_data = [train_df , test_df]
full_data
train_df.info()
#1.PClass
train_df[['Pclass','Survived']].groupby(['Pclass'],as_index = 'False').mean()
#2.Sex
train_df[['Sex','Survived']].groupby(['Sex'],as_index = 'False').mean()
#3.SibSp and Parch -Sibling/Spouse, Parent/Children

for dataset in full_data:
    dataset['FamilySize'] = dataset['SibSp'] + dataset['Parch'] + 1

train_df[['FamilySize','Survived']].groupby(['FamilySize'],as_index = 'False').mean()

#4.Categorize people as per their lonliness

for dataset in full_data:
    dataset['IsAlone'] = 0
    dataset.loc[dataset['FamilySize'] == 1,'IsAlone'] = 1
train_df[['IsAlone','Survived']].groupby(['IsAlone'],as_index='False').mean()

"""
Feature Engineering
"""
df.info()
df.describe()
#Family Size

df['FamilySize'] = df ['SibSp']+df['Parch']+1

#Name Length

df['NameLength'] = df['Name'].apply(len)

#IsAlone?
df['IsAlone'] = 0
df.loc[df['FamilySize']==1,'IsAlone'] = 1
df
#Title 

df['Title'] = 0
df['Title'] = df.Name.str.extract('([A-Za-z]+)\.',expand=True)
df['Title'].replace(['Mlle','Mme','Ms','Dr','Major','Lady','Countess','Jonkheer','Col','Rev','Capt','Sir','Dona'],['Miss','Miss','Miss','Mr','Mr','Mrs','Mrs','Other','Other','Other','Mr','Mr','Mr'],inplace=True)
df[['Title','Age']].groupby(['Title'],as_index= 'False').mean()

#Age

df.loc[(df.Age.isnull()) & (df.Title=='Mr'),'Age']=df.Age[df.Title=='Mr'].mean()
df.loc[(df.Age.isnull()) & (df.Title=='Mrs'),'Age']=df.Age[df.Title=='Mrs'].mean()
df.loc[(df.Age.isnull()) & (df.Title=='Miss'),'Age']=df.Age[df.Title=='Miss'].mean()
df.loc[(df.Age.isnull()) & (df.Title=='Master'),'Age']=df.Age[df.Title=='Master'].mean()
df.loc[(df.Age.isnull()) & (df.Title=='Other'),'Age']=df.Age[df.Title=='Other'].mean()

df =df.drop('Name',axis=1)



