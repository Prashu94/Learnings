# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 17:14:54 2018

@author: Prashant Bhat
"""

#Domain – Retail/Fashion

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model 
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error

"""
Import Data from FyntraCustomerData.csv
"""
path = "G:\\extra things\\Knowledge\\practice\\Edureka\\Module6\\"
f_data  = pd.read_csv(path+"FyntraCustomerData.csv")

f_data.columns
f_data.head(1)

"""
1. Compute -- Use seaborn to create a jointplot to compare the Time on Website and Yearly Amount Spent columns. \
Is there a correlation?
Yes as the corerlation is 0.95 which is near to +1
"""

x = np.array(f_data['Yearly_Amount_Spent'])
y = np.array(f_data['Time_on_Website'])

sns.jointplot(x,y)

"""
2. Compute – Do the same as above but now with Time on App and Yearly Amount Spent. 
Is this correlation stronger than 1st One?
There is negative coreraltion hence it is stronger than the 1st one
"""

x1 = np.array(f_data['Yearly_Amount_Spent'])
y1 = np.array(f_data['Time_on_App'])

sns.jointplot(x1,y1)

"""
3. Compute -- Explore types of relationships across the entire data set using pairplot . 
Based off this plot what looks to be the most correlated feature with Yearly Amount Spent?
"""

sns.pairplot(f_data)


"""
4. Compute – Create linear model plot of Length of Membership and Yearly Amount Spent. 
Does the data fits well in linear plot?
Best Fit
"""
f_data['Length_of_Membership'].describe()
f_data['Yearly_Amount_Spent'].describe()

linear_df = f_data.loc[:,['Length_of_Membership','Yearly_Amount_Spent']]

l_dataset = linear_df.as_matrix()

l_dataset.shape

x = l_dataset[:,:-1]
y = l_dataset[:,0]
print(x.shape)
print(y.shape)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size =0.25,random_state =5)

print(x_train.shape,y_train.shape)

lr = linear_model.LinearRegression()

model = lr.fit(x_train,y_train)
print(model)

lr.score(x_test,y_test)

plt.figure(figsize = (20,20))
plt.plot(x_train,y_train)
plt.show()


y_predict = lr.predict(x_test)
print(y_predict)

y_predict - y_test


"""
5. Compute – Train and Test the data and answer multiple questions -- What is the use of random_state=85?
"""

f_data['Length_of_Membership'].describe()
f_data['Yearly_Amount_Spent'].describe()

linear_df = f_data.loc[:,['Length_of_Membership','Yearly_Amount_Spent']]

l_dataset = linear_df.as_matrix()

l_dataset.shape

x = l_dataset[:,:-1]
y = l_dataset[:,0]
print(x.shape)
print(y.shape)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size =0.25,random_state =85)

print(x_train.shape,y_train.shape)

lr = linear_model.LinearRegression()

model = lr.fit(x_train,y_train)
print(model)

lr.score(x_test,y_test)

plt.figure(figsize = (5,5))
plt.plot(x_train,y_train)
plt.show()


y_predict = lr.predict(x_test)
print(y_predict)

y_predict - y_test


plt.figure(figsize = (5,5))
plt.scatter(x_test,y_predict)
plt.show()


"""
7. What is the value of Root Mean Squared Error?
"""
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test,y_predict)

print(mse)

"""
8. Final Question – Based on coefficients interpret company should focus more on their mobile app or on their website

The company must focus more on WebApps
"""



