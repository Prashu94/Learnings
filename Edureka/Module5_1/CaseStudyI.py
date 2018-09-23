# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 19:42:54 2018

@author: Prashant Bhat
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""
Data Provided on Hollywood Movies
"""

path = "G:\\extra things\\Knowledge\\practice\\Edureka\\Module5\\"
h_data = pd.read_csv(path+"HollywoodMovies.csv")

h_data.head()
h_data.describe()

#1.Find the highest Rated movie in Quest story type
"""
Selcting data for quest story type
"""

s_quest=h_data[h_data['Story']=='Quest']
s_quest['TotalRating'] = (s_quest['RottenTomatoes']+s_quest['AudienceScore'])/2
s_sorted_quest= s_quest.sort_index(by = 'TotalRating',ascending=False)
"""
The Muppets-- This as per average rating of audience and rotten tomatoes
"""
s_sorted_quest['Movie'].head(1)

#Find the genre in which there has been the greatest number of movies release
h_data.head(2)
select_m_data = h_data.loc[:,['Movie','Genre']]
select_m_data.groupby(['Genre'],as_index=False).agg({'Movie':'count'})

#Print the name of top five movies with the costliest budget
select_m_data1 = h_data.loc[:,['Movie','Budget']]
sorted_m_data1=select_m_data1.sort_values(by = 'Budget',ascending=False)
sorted_m_data1.head(5)

#Correlation between critics evaluation and its acceptence by the public 
#Find out by plotting the net profitabality of a movie against the ratings it receives on rottent tomatoes

plt.figure(figsize=(20,20))
selected_data = h_data.loc[:,['Profitability','RottenTomatoes']]
x=np.array(selected_data["Profitability"])
y=np.array(selected_data["RottenTomatoes"])
plt.scatter(x,y)
plt.xlabel("Profitability")
plt.ylabel("RottenTomatoes")
plt.title("Correaltion")
plt.show()

"""
Creating a dataframe 
"""

data1 = {'first_name':pd.Series(['Jason', 'Molly', 'Tina', 'Jake', 'Amy']),
         'last_name':pd.Series(['Miller', 'Jacobson', ".", 'Milner', 'Cooze']),
         'age':pd.Series([42, 52, 36, 24, 73]),
         'preTestScore':[4, 24, 31, ".", "."],
         'postTestScores':["25,000", "94,000", 57, 62, 70]
        }
raw_data1 = pd.DataFrame(data1)
raw_data1.to_csv("example.csv")

df1 = pd.read_csv("example.csv")
df1.head()
df1
#Read the example.csv and make the index columns as 'First Name’ and 'Last Name'
df2  = pd.read_csv("example.csv")
df2.set_index((['first_name','last_name']))
#Read the dataframe by skipping first 3 rows and print the data frame
df3 = pd.read_csv("example.csv")[3:]
df3

"""
From the raw data below create a Pandas Series 'Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'
"""
series1 = pd.Series(['Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'])
series1.dropna()
series1.str.upper()
series1.str.lower()
series1.str.len()


"""
From the raw data below create a Pandas Series ' Atul', 'John ', ' jack ', 'Sam'
"""

series2 = pd.Series([' Atul', 'John ', ' jack ', 'Sam'])
series2.str.strip()
series2.str.lstrip()
series2.str.rstrip()

"""
Create a series from the raw data below 'India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'
"""

series3 = pd.Series(['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'])
list_series = list(series3.str.split('_'))
print(list_series)
print(list_series[1:])


"""
'A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat'
"""
series4 = pd.Series(['A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat'])
series4.dropna()
series4.str.replace('X','XX-XX')
series4.str.replace('dog','XX-XX')

"""
Create a series and reverse all lower case words 'india 1998', 'big country', np.nan
"""
series5 =pd.Series(['india 1998', 'big country', np.nan])
if series5.str.islower:
    print(series5.str[::-1])

"""
Create pandas series and print true if value is alphanumeric in series or false if value is not alpha numeric in series.
"""

series6 = pd.Series(['1', '2', '1a', '2b', '2003c'])
if series6.str.isalnum:
    print(True)
else:
    print(False)
"""
Create pandas series and print true if value is containing ‘A’
"""
series7 = pd.Series(['1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'])
for i in range(len(series7)):
    if series7[i].str.contains('A'):
        print (True)
    else:
        print(False)
"""
Create pandas dataframe having keys and ltable and rtable as below - 
'key': ['One', 'Two'], 'ltable': [1, 2] 'key': ['One', 'Two'], 'rtable': [4, 5]
"""
pd_df1 = {
        'key':pd.Series(['One', 'Two']),
        'ltable':pd.Series([1, 2])
        }
daf1 = pd.DataFrame(pd_df1)

pd_df2 = {
        'key':pd.Series(['One', 'Two']),
        'rtable':pd.Series([4, 5])
        }
daf2= pd.DataFrame(pd_df2)

pd.merge(daf1,daf2,on='key')