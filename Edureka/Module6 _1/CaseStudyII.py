# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 22:11:22 2018

@author: Prashant Bhat
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = "G:\\extra things\\Knowledge\\practice\\Edureka\\Module6\\"
c_data = pd.read_csv(path+"cereal.csv")
c_data1= c_data
c_data.head(1)
len(c_data.columns.tolist())
c_select_data  = c_data.loc[:,['Sugars','vitamins','name']]
"""
1.Load the data from “cereal.csv” and plot histograms of sugar and vitamin content across different cereals.
"""
plt.hist(c_select_data)
plt.show()


df1 = {
       'mfr':pd.Series(['N','Q','K','R','G','P','A']),
       'full_name':pd.Series(['Nabisco','Quaker Oats','Kellogs','Raslston Purina','General Mills','Post','American Home Food Products'])
       }
df_1 = pd.DataFrame(df1)
c_data1_select =c_data1.loc[:,['mfr']]
joined_data = pd.merge(df_1,c_data1_select, on ='mfr',how = 'inner')

c_data['Full_Name'] = joined_data['full_name']
c_data.head(1)


"""
Fit a linear regression module and measure the mean squared error on test dataset.
"""
from sklearn.cross_validation import train_test_split
c_df = c_data.iloc[:,3:-1]

dataset = c_df.as_matrix()
dataset.shape

x = dataset [:,:-1]
y = dataset [:,-1]

x.shape
y.shape

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size =0.25,random_state =5)
print(x_train.shape)
print(y_train.shape)
from sklearn import linear_model 

lm = linear_model.LinearRegression()
model = lm.fit(x_train,y_train)

lm.score(x_test,y_test)

predict_y = lm.predict(x_test)

predict_y - y_test

lm.get_params()

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test,predict_y)

print(mse)





