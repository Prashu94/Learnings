# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 20:32:47 2018

@author: Prashant Bhat
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
"""
Data Loading
"""

#Q1a. Load the dataset “prisoners.csv” using pandas and display the first and last five rows in the dataset.

path = "G:\\extra things\\Knowledge\\practice\\Edureka\\Module6\\"
p_data = pd.read_csv(path+"prisoners.csv")

#First five Rows
p_data.head(5)
#Last five rows
p_data.tail(5)
"""
#Q1b. Use describe method in pandas and find out the number of columns. 
Can you say something about those rows who have zero inmates?
"""
#Describe method
p_data.describe()
print(len(p_data.columns.tolist()))
p_data[p_data['No. of Inmates benefitted by Elementary Education'] == 0]
p_data[p_data['No. of Inmates benefitted by Adult Education'] == 0]
p_data[p_data['No. of Inmates benefitted by Higher Education'] == 0]
p_data[p_data['No. of Inmates benefitted by Computer Course'] == 0]


"""
Data Manipulation
"""
#2a. Create a new column -’total_benefitted’ that is a sum of inmates benefitted through all modes.
p_select_data = p_data.iloc[:,2:5]
p_select_data.head(1)
p_select_data['total_benefitted'] = p_select_data.sum(axis=1)
p_data['total_benefitted'] = p_select_data['total_benefitted']
p_data.head(1)
"""
#2b. Create a new row - “totals” that 
is the sum of all inmates benefitted through each mode across all states.
"""
p_select_data1 = p_data.loc[:,['total_benefitted','STATE/UT']]
p_sort_data=p_select_data1.groupby(['STATE/UT'],as_index =False).agg({'total_benefitted':'sum'}).sort_values(by='total_benefitted',ascending=False)

"""
Plotting
"""

"""
a. Make a bar plot with each state name on the x -axis and their 
total benefitted inmates as their bar heights. Which state has the maximum number of beneficiaries?
"""
plt.figure(figsize=(10,10))
x = np.array(p_data['STATE/UT'])
y = np.array(p_data['total_benefitted'])
plt.bar(x,y)
plt.xlabel('STATE/UT')
plt.ylabel('Benefitted')
plt.title('STATE and Prisoners')
plt.show()

"""
The basic data loading, data wrangling and visualization was asked which was answered using the pandas, numpy and matplotlib
"""