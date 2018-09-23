# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 23:13:31 2018

@author: Prashant Bhat
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
path = "G:\\extra things\\Knowledge\\practice\\Edureka\\Module5\\"
s_data = pd.read_csv(path+"Salaries.csv")
s_data.head()

"""
Preparing the data by filling NaN's with mean values
"""
#Copy of the the origincal dataframe
s_data1 = s_data
s_data1.head()
#Extracts the columns haveing null value
s_data1.columns[s_data1.isnull().any()].tolist()

s_data1=s_data1.drop(['Notes'],axis=1)

s_data1['Benefits'].fillna((s_data1['Benefits'].mean()),inplace=True)
s_data1['Benefits'].head(2)

mode = s_data1['Status'][0]
s_data1['Status'] = s_data1.groupby('Status')

s_data1.head()
select_data1 = s_data1.loc[:,['TotalPayBenefits','Year']]
select_data1.head()
select_data_2011 = select_data1[select_data1['Year'] == 2011]
select_data_2014 = select_data1[select_data1['Year'] == 2014]

increase_in_salary = (select_data_2014['TotalPayBenefits'].sum()-select_data_2011['TotalPayBenefits'].sum())

print(increase_in_salary)


s_data1.head(1)
s_data2_2014 =s_data1[s_data1['Year']==2014]
select_c_2014 = s_data2_2014.loc[:,['TotalPay','JobTitle']]
s_2014 = select_c_2014.groupby(['JobTitle'],as_index=False).agg({'TotalPay':'mean'})
s_2014_sort = s_2014.sort_values(by = 'TotalPay',ascending =False)
"""
Chief Investment Officer
"""


