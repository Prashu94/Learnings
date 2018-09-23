# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 18:09:32 2018

@author: Prashant Bhat
"""

"""
1.
Extract data from the given
SalaryGender 
CSV file and store the data from each 
column in a separate NumPy array
"""

import pandas as pd, numpy as np

path = "G:\\extra things\\Knowledge\\practice\\Edureka\\Module4\\"
salary_gender_data = pd.read_csv(path+"SalaryGender.csv")

salary_gender_data.head()
array_convert= np.array(salary_gender_data)
print(array_convert)


"""
2.
Find:
1. The number of men with a PhD
2. The number of women with a PhD
0-Male
1-Female
"""
salary_gender_data.groupby('Gender')['PhD'].sum()

"""
3.
Use 
SalaryGender CSV file. 
Store the “Age” and “PhD” columns in one DataFrame 
and delete the data of all people who don’t have a PhD
"""
new_data_frame = salary_gender_data[['Age','PhD']]
only_phd_group = new_data_frame[new_data_frame['PhD']==1]
print(only_phd_group)

"""
4.
Calculate the total number of people who have a PhD degree
from SalaryGender 
CSV file.
"""

salary_gender_data[salary_gender_data['PhD']==1].count()['Gender']

"""
5.
How  do  you  Count  The  Number  Of  Times  E
ach  Value  Appears  In  An  Array  Of 
Integers?
[0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9
"""

list1 = [0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]
for i in range(len(list1)):
    print (list1[i],':',list1.count(list1[i]))


"""
6.
Create a numpy
array [[0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],[ 9,
10, 11]]) and filter the elements 
greater than 5
.
"""

list2 =[[0, 1, 2],
         [ 3, 4, 5],
         [ 6, 7, 8],
         [ 9,10, 11]]
arrays1 = np.array(list2)
n,m=arrays1.shape
for i in range(n):
    for j in range(m):
        if (arrays1[i,j] > 5):
            print(arrays1[i,j])
"""
7.
C
reate a numpy array having NaN (Not a Number) and print it
.
array([ nan,   1.,   2.,  nan,   3.,   4.,   5.])
"""
from numpy import nan
arrays2 = np.array([ nan,   1.,   2.,  nan,   3.,   4.,   5.])
arrays2 = arrays2[~np.isnan(arrays2)]
print(arrays2)

"""
8.
Create  a  10x10  array  with  random  values  and  find  the  minimum  and  maximum 
values
"""

arrays3 = np.random.random((5,5))
print("Original array:")
print(arrays3)
xmin,xmax = arrays3.min(),arrays3.max()
print("Minimum:",xmin,"Maximum:",xmax)

"""
9.
Create a random vector of size 30 and find the mean value.
"""

vector1 = np.linspace(0,30,1)
print(vector1.mean())

"""
10.
Create numpy array having elements 0 to 10 And negate all the elements between 
3 and 9
"""
arrays4 = np.arange(10)
arrays4

"""
11.
Create a random array of 3 rows and 3 columns and sort it according to 1
st
column, 
2
nd
column or 3
rd
column
.
"""
arrays5 = np.random.random((3,3))
np.sort(arrays5.view('i8,i8,i8'),order=['f1'],axis=0).view(np.int)

"""
12.Create a four dimensional array get sum over the last two axis at once
"""

arrays6 = np.arange(0,16).reshape(4,4)
arrays6.sum(axis=(0,1),keepdims =True)
print(arrays6)

"""
Create a random array and swap two rows of an array
.
"""
a = np .random.randint(0,10,(2,3,3))
b = np .random.randint(0,10,(2,5,5))

#display before

a[:,0,0]
b[:,0,0]
#After Swap
a[:,0,0],b[:,0,0]=b[:,0,0],a[:,0,0]

a[:,0,0]
b[:,0,0]


