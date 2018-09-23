# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 20:35:33 2018

@author: Prashant Bhat
"""
"""
Import the required packages/modules
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.decomposition import PCA
###############################################################################
"""
Loading the dataset
"""
path = "G:\\extra things\\Knowledge\\practice\\Edureka\\Module9\\"
data = pd.read_csv(path+"run_or_walk.csv")

"""
Explore the dataset
"""
data.head(1)
data.describe()
data.info()
"""
Below checks for null columns in the dataset
"""
null_columns = dict(data.isnull().any()[lambda x:x])
print(null_columns)
#0-left , 1 -right
data.groupby('wrist').groups.keys()
print('Dataset contains ' + str(pd.value_counts(data['wrist'].values)[0])+ ' "left wrist" data samples as well as' +str(pd.value_counts(data['wrist'].values)[1])+ ' "right wrist" samples')
#0-walk,1-run
data.groupby('activity').groups.keys()
print('Dataset contains ' + str(pd.value_counts(data['activity'].values)[0])+ ' "walk" data samples as well as' +str(pd.value_counts(data['activity'].values)[1])+ ' "run" samples')

"""
Data skewness check
"""
#Wirst Types
LEFT_WRIST = 0
RIGHT_WRIST =1 

#Populate the dataframe with 'walk' data only
df_data_walk = pd.DataFrame()
df_data_walk = data[(data.activity == 0)]

#Populate the dataframe with 'run' data only

df_data_run = pd.DataFrame()
df_data_run = data[(data.activity ==1)]

walk_data_left_wrist_count = pd.value_counts(df_data_walk['wrist'].values,sort=False)[LEFT_WRIST]
walk_data_right_wrist_count = pd.value_counts(df_data_walk['wrist'].values,sort=False)[RIGHT_WRIST]

run_data_left_wrist_count = pd.value_counts(df_data_run['wrist'].values,sort=False)[LEFT_WRIST]
run_data_right_wrist_count = pd.value_counts(df_data_run['wrist'].values,sort=False)[RIGHT_WRIST]
#right wrist samples > left_wrist_samples
print ('Total number of "walk" data samples:' +str(len(df_data_walk)))
print('  Number of left wrist samples:' + str(walk_data_left_wrist_count))
print('  Number of right wrist samples:' + str(walk_data_right_wrist_count))
print('Total number of "run" data samples:' +str(len(df_data_run)))
print('  Number of left wrist samples:' + str(run_data_left_wrist_count))
print('  Numberof right wrist samples:' + str(run_data_right_wrist_count))

"""
Numerical Data Distribution
"""
SENSOR_DATA_COLUMNS = ['acceleration_x', 'acceleration_y', 'acceleration_z', 'gyro_x', 'gyro_y', 'gyro_z']

#populate dataframe with 'left; wrist only
df_left_wrist_data = pd.DataFrame()
df_left_wrist_data = data[data.wrist == 0]

#populate dataframe with 'left; wrist only
df_right_wrist_data = pd.DataFrame()
df_right_wrist_data = data[data.wrist == 1]

for c in SENSOR_DATA_COLUMNS:
    plt.figure(figsize=(10,5))
    plt.title('Sensor Data distribution for both wrist')
    sns.distplot(df_left_wrist_data[c],label ='left')
    sns.distplot(df_right_wrist_data[c],label='right')
    plt.legend()
    plt.show()

"""
Clean the dataframe with unwanted attributes
"""

cleaned_df = data.drop(['username'],axis=1)
cleaned_df['date'] = pd.to_datetime(cleaned_df['date'])
cleaned_df['weekdays'] = cleaned_df['date'].dt.weekday
cleaned_df = cleaned_df.drop(['date'],axis=1)

cleaned_df['hours'] = cleaned_df['time'].str.extract('(\d\d)', expand=True).astype(float)
cleaned_df['minutes'] = cleaned_df['time'].str.extract('[\d\d\:](\d\d)', expand=True).astype(float)
cleaned_df['hours'] = cleaned_df['hours'] + cleaned_df['minutes'] / 60

cleaned_df = cleaned_df.drop(['time'], axis=1)
cleaned_df = cleaned_df.drop(['minutes'], axis=1)
cleaned_df.head()

"""
Splitting the data into train and test
"""

X = cleaned_df.drop(['activity'],axis=1)
y = cleaned_df['activity'].copy()

"""
Visualiztion using PCA
"""
pca = PCA(n_components=2)
X_trans = pca.fit(X).transform(X)
walk = plt.scatter(X_trans[y == 0, 0], X_trans[y == 0, 1], label="walk")
run = plt.scatter(X_trans[y == 1, 0], X_trans[y == 1, 1], label="run")
plt.legend((walk, run), ('walk', 'run'))
plt.title('PCA')
plt.xlabel('First Component')
plt.ylabel('Second Component')
plt.show()


"""
Model Training
"""

x_train,x_test,y_train,y_test = train_test_split(X,y,test_size = 0.1, random_state =0)

#Model NaiveBayes

naive_bayes = GaussianNB()
naive_bayes.fit(x_train, y_train)
print("The training accuracy for Gaussian Naive Bayes is ", naive_bayes.score(x_train, y_train))
print("The testing accuracy for Gaussian Naive Bayes is ", naive_bayes.score(x_test, y_test))


#Using acceleration values as predictors

"""
Splitting the data into train and test
"""

X1 = cleaned_df.drop(['activity','gyro_x','gyro_y','gyro_z'],axis=1)
y1 = cleaned_df['activity'].copy()

X1.head(1)
"""
Visualiztion using PCA
"""
pca = PCA(n_components=2)
X_trans1 = pca.fit(X1).transform(X1)
walk = plt.scatter(X_trans1[y1 == 0, 0], X_trans1[y1 == 0, 1], label="walk")
run = plt.scatter(X_trans1[y1 == 1, 0], X_trans1[y1 == 1, 1], label="run")
plt.legend((walk, run), ('walk', 'run'))
plt.title('PCA')
plt.xlabel('First Component')
plt.ylabel('Second Component')
plt.show()


"""
Model Training
"""

x_train1,x_test1,y_train1,y_test1 = train_test_split(X1,y1,test_size = 0.1, random_state =0)

#Model NaiveBayes

naive_bayes = GaussianNB()
naive_bayes.fit(x_train1, y_train1)
print("The training accuracy for Gaussian Naive Bayes is ", naive_bayes.score(x_train1, y_train1))
print("The testing accuracy for Gaussian Naive Bayes is ", naive_bayes.score(x_test1, y_test1))


#Using gyro values as predictors

"""
Splitting the data into train and test
"""

X2 = cleaned_df.drop(['activity','acceleration_x','acceleration_y','acceleration_z'],axis=1)
y2 = cleaned_df['activity'].copy()

X2.head(1)
"""
Visualiztion using PCA
"""
pca = PCA(n_components=2)
X_trans2 = pca.fit(X2).transform(X2)
walk = plt.scatter(X_trans2[y2 == 0, 0], X_trans2[y2 == 0, 1], label="walk")
run = plt.scatter(X_trans2[y2 == 1, 0], X_trans1[y2 == 1, 1], label="run")
plt.legend((walk, run), ('walk', 'run'))
plt.title('PCA')
plt.xlabel('First Component')
plt.ylabel('Second Component')
plt.show()


"""
Model Training
"""

x_train2,x_test2,y_train2,y_test2 = train_test_split(X2,y2,test_size = 0.1, random_state =0)

#Model NaiveBayes

naive_bayes = GaussianNB()
naive_bayes.fit(x_train2, y_train2)
print("The training accuracy for Gaussian Naive Bayes is ", naive_bayes.score(x_train2, y_train2))
print("The testing accuracy for Gaussian Naive Bayes is ", naive_bayes.score(x_test2, y_test2))
