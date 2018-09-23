# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 22:46:44 2018

@author: Prashant Bhat
"""

import pandas as pd
import matplotlib.pyplot as plt

path = "G:\\extra things\\Knowledge\\practice\\Edureka\\Module4\\"
retail_data = pd.read_csv(path+"BigMartSalesData.csv")
retail_data.head()

data_2011 = retail_data[retail_data.Year == 2011]
data_2011['Sales'] = data_2011['Amount'] * data_2011['Quantity'] * data_2011['UnitPrice']
plt_data = data_2011.groupby(['Month'],as_index =False).agg({'Sales':'sum'})
plt_data
plt.bar(plt_data['Month'],plt_data['Sales'])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Total Sales Per Month")
plt.show()

#Pie Chart
plt_country = data_2011.groupby(['Country'],as_index=False).agg({'Sales':'sum'})
plt_country
plt.pie(plt_country['Sales'])
plt.show()

#Scatter Plot
data_2011.head()
plt.scatter(data_2011['InvoiceNo'],data_2011['Amount'])
plt.show()