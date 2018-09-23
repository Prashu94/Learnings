# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 14:02:48 2018

@author: Prashant Bhat
"""

"""
Loading all the required libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn import tree
##############################################################################
"""
1. Let’s attempt to predict the survival of a horse based on various observed medical conditions. 
Load the data from ‘horses.csv’ and observe whether it contains missing values.
"""

#Loading the horse data
path = "G:\\extra things\\Knowledge\\practice\\Edureka\\Module7\\"
horse = pd.read_csv(path+"horse.csv")

horse.columns
horse_copy = horse

"""
Exploring the dataset
"""
    
horse.describe()
horse.dtypes
#Printing columns having null values

null_columns = dict(horse.isnull().any()[lambda x:x])
print(null_columns)
"""
{'rectal_temp': True, 'pulse': True, 'respiratory_rate': True, 
'temp_of_extremities': True, 'peripheral_pulse': True, 
'mucous_membrane': True, 'capillary_refill_time': True, 
'pain': True, 'peristalsis': True, 
'abdominal_distention': True, 
'nasogastric_tube': True, 
'nasogastric_reflux': True, 'nasogastric_reflux_ph': True, 
'rectal_exam_feces': True, 'abdomen': True, 'packed_cell_volume': True, 
'total_protein': True, 'abdomo_appearance': True, 'abdomo_protein': True}
"""
null_list = list(null_columns.keys())

horse[null_list].dtypes

"""
rectal_temp              float64
pulse                    float64
respiratory_rate         float64
temp_of_extremities       object
peripheral_pulse          object
mucous_membrane           object
capillary_refill_time     object
pain                      object
peristalsis               object
abdominal_distention      object
nasogastric_tube          object
nasogastric_reflux        object
nasogastric_reflux_ph    float64
rectal_exam_feces         object
abdomen                   object
packed_cell_volume       float64
total_protein            float64
abdomo_appearance         object
abdomo_protein           float64
"""

horse['rectal_temp']=horse['rectal_temp'].fillna(horse['rectal_temp'].mean())
horse['pulse']=horse['pulse'].fillna(horse['pulse'].mean())
horse['respiratory_rate']=horse['respiratory_rate'].fillna(horse['respiratory_rate'].mean())
horse['nasogastric_reflux_ph'] = horse['nasogastric_reflux_ph'].fillna(horse['nasogastric_reflux_ph'].mean())
horse['packed_cell_volume'] = horse['packed_cell_volume'].fillna(horse['packed_cell_volume']).mean()
horse['total_protein'] = horse['total_protein'].fillna(horse['total_protein'].mean())
horse['abdomo_protein'] = horse['abdomo_protein'].fillna(horse['abdomo_protein'].mean())


#Categorical variable replaced with mode where it is null
horse['temp_of_extremities'] = horse['temp_of_extremities'].fillna(horse['temp_of_extremities'].mode().iloc[0])
horse['peripheral_pulse'] = horse['peripheral_pulse'].fillna(horse['peripheral_pulse'].mode().iloc[0])
horse['mucous_membrane'] = horse['mucous_membrane'].fillna(horse['mucous_membrane'].mode().iloc[0])
horse['capillary_refill_time'] = horse['capillary_refill_time'].fillna(horse['capillary_refill_time'].mode().iloc[0])
horse['pain'] = horse['pain'].fillna(horse['pain'].mode().iloc[0])
horse['peristalsis'] = horse['peristalsis'].fillna(horse['peristalsis'].mode().iloc[0])
horse['abdominal_distention'] = horse['abdominal_distention'].fillna(horse['abdominal_distention'].mode().iloc[0])
horse['nasogastric_tube'] = horse['nasogastric_tube'].fillna(horse['nasogastric_tube'].mode().iloc[0])
horse['nasogastric_reflux'] = horse['nasogastric_reflux'].fillna(horse['nasogastric_reflux'].mode().iloc[0])
horse['rectal_exam_feces'] = horse['rectal_exam_feces'].fillna(horse['rectal_exam_feces'].mode().iloc[0])
horse['abdomen'] = horse['abdomen'].fillna(horse['abdomen'].mode().iloc[0])
horse['abdomo_appearance'] = horse['abdomo_appearance'].fillna(horse['abdomo_appearance'].mode().iloc[0])

"""
Using Preprocessing, to encode values
"""
horse.groupby('temp_of_extremities').groups.keys()

le = preprocessing.LabelEncoder()
le.fit(horse['temp_of_extremities'])
le.classes_
horse['temp_of_extremities']=le.transform(horse['temp_of_extremities'])

le = preprocessing.LabelEncoder()
le.fit(horse['peripheral_pulse'])
le.classes_
horse['peripheral_pulse']=le.transform(horse['peripheral_pulse'])

horse.groupby('peripheral_pulse').groups.keys()

le = preprocessing.LabelEncoder()
le.fit(horse['mucous_membrane'])
le.classes_
horse['mucous_membrane']=le.transform(horse['mucous_membrane'])

horse.groupby('mucous_membrane').groups.keys()

le = preprocessing.LabelEncoder()
le.fit(horse['capillary_refill_time'])
le.classes_
horse['capillary_refill_time']=le.transform(horse['capillary_refill_time'])

horse.groupby('capillary_refill_time').groups.keys()

le = preprocessing.LabelEncoder()
le.fit(horse['pain'])
le.classes_
horse['pain']=le.transform(horse['pain'])

horse.groupby('pain').groups.keys()

le = preprocessing.LabelEncoder()
le.fit(horse['peristalsis'])
le.classes_
horse['peristalsis']=le.transform(horse['peristalsis'])

horse.groupby('peristalsis').groups.keys()

le = preprocessing.LabelEncoder()
le.fit(horse['abdominal_distention'])
le.classes_
horse['abdominal_distention']=le.transform(horse['abdominal_distention'])

horse.groupby('abdominal_distention').groups.keys()

le = preprocessing.LabelEncoder()
le.fit(horse['nasogastric_tube'])
le.classes_
horse['nasogastric_tube']=le.transform(horse['nasogastric_tube'])

horse.groupby('nasogastric_tube').groups.keys()

le = preprocessing.LabelEncoder()
le.fit(horse['nasogastric_reflux'])
le.classes_
horse['nasogastric_reflux']=le.transform(horse['nasogastric_reflux'])

horse.groupby('nasogastric_reflux').groups.keys()

le = preprocessing.LabelEncoder()
le.fit(horse['rectal_exam_feces'])
le.classes_
horse['rectal_exam_feces']=le.transform(horse['rectal_exam_feces'])

horse.groupby('rectal_exam_feces').groups.keys()

le = preprocessing.LabelEncoder()
le.fit(horse['abdomen'])
le.classes_
horse['abdomen']=le.transform(horse['abdomen'])

horse.groupby('abdomen').groups.keys()

le = preprocessing.LabelEncoder()
le.fit(horse['abdomo_appearance'])
le.classes_
horse['abdomo_appearance']=le.transform(horse['abdomo_appearance'])

horse.groupby('abdomo_appearance').groups.keys()


le = preprocessing.LabelEncoder()
le.fit(horse['outcome'])
le.classes_
horse['outcome']=le.transform(horse['outcome'])

horse.groupby('outcome').groups.keys()

le = preprocessing.LabelEncoder()
le.fit(horse['surgery'])
le.classes_
horse['surgery']=le.transform(horse['surgery'])

horse.groupby('surgery').groups.keys()

le = preprocessing.LabelEncoder()
le.fit(horse['age'])
le.classes_
horse['age']=le.transform(horse['age'])

horse.groupby('age').groups.keys()


le = preprocessing.LabelEncoder()
le.fit(horse['surgical_lesion'])
le.classes_
horse['surgical_lesion']=le.transform(horse['surgical_lesion'])

horse.groupby('surgical_lesion').groups.keys()


le = preprocessing.LabelEncoder()
le.fit(horse['cp_data'])
le.classes_
horse['cp_data']=le.transform(horse['cp_data'])
horse.groupby('cp_data').groups.keys()

prediction_var = horse.columns
print(list(prediction_var))
#Train Test split
X = horse.drop('outcome',axis=1)
Y = horse['outcome']

train,test = train_test_split(horse,test_size=0.3)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size =0.3 ,random_state=101)


print(train.shape)
print(test.shape)

train_X=  train[prediction_var]
train_Y= train['outcome']

test_X= test[prediction_var]
test_Y= test['outcome']


"""
Building Models
"""
#RandomForest classifier
model=RandomForestClassifier(n_estimators=100)
model.fit(train_X,train_Y)
prediction=model.predict(test_X)
print(metrics.accuracy_score(prediction,test_Y)) 


model2 = RandomForestClassifier(n_estimators=600)
model2.fit(X_train,Y_train)
prediction1 = model2.predict(X_test)
print(classification_report(Y_test,prediction1))
print(accuracy_score(prediction1,Y_test))

#Decision Tree
model_t = tree.DecisionTreeClassifier()
model_t.fit(train_X,train_Y)

prediction=model.predict(test_X)

df_horse = pd.DataFrame(prediction,test_Y)
print(df_horse)

print(metrics.accuracy_score(prediction,test_Y))

model_t1 = tree.DecisionTreeClassifier()
model_t1.fit(X_train,Y_train)
prediction2 = model_t1.predict(X_test)
print(classification_report(Y_test,prediction2))
print(accuracy_score(prediction2,Y_test))