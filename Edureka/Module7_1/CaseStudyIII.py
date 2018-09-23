# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 20:32:04 2018

@author: Prashant Bhat
"""

"""
Loading all the required modules
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn import tree
##############################################################################

"""
Loading the data
"""

path = "G:\\extra things\\Knowledge\\practice\\Edureka\\Module7\\"
bank = pd.read_csv(path+"loan_borowwer_data.csv")


bank.columns = ['credit_policy','purpose','int_rate','installment','log_annual_inc','dti','fico','days_with_cr_line','revol_bal','revol_util','inq_last_6mnths','dlinq_2yrs','pub_rec','not_fully_paid']
bank.dtypes

#This checks if there is any null columns, here the output is no null columns
null_columns = dict(bank.isnull().any()[lambda x:x])

bank.groupby('purpose').groups.keys()

le = preprocessing.LabelEncoder()
le.fit(bank['purpose'])
le.classes_
bank['purpose']=le.transform(bank['purpose'])

prediction_var = bank.columns
print(list(prediction_var))
#Train Test split

train,test = train_test_split(bank,test_size=0.3)

print(train.shape)
print(test.shape)

train_X=  train[prediction_var]
train_Y= train['not_fully_paid']

test_X= test[prediction_var]
test_Y= test['not_fully_paid']

sns.heatmap(bank.corr(), annot=True, fmt=".2f")


"""
Building Models
"""
#RandomForest classifier
model=RandomForestClassifier(n_estimators=100)
model.fit(train_X,train_Y)
prediction=model.predict(test_X)
print(metrics.accuracy_score(prediction,test_Y)) 

df_bank = pd.DataFrame(prediction,test_Y)
print(df_bank)

