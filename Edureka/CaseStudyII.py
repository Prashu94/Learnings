# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 18:34:42 2018

@author: Prashant Bhat
"""

"""
Reading file bank-data.csv
"""

import pandas as pd
path = "G:\\extra things\\Knowledge\\practice\\Edureka\\Module3\\"
bank_data = pd.read_csv(path+"bank-data.csv")
bank_data.head()

"""
Set of unique jobs
"""
unique_jobs = bank_data['job'].unique()
print(unique_jobs)

"""
Reading input from command line -profession
Make the profession check case insensitive
"""

profession = input("Enter the profession:")

if (profession.lower() in unique_jobs):
    print("Eligible")
else:
    print("Not Eligible")


"""
Code Enhancements
"""

"""
Computing max and min age for loan eligibility based on the data in csv file
"""

max_age=max(bank_data['age'])
min_age=min(bank_data['age'])

"""
Store Max and min age in dictionary
"""
dict_max_min ={"max_age":max_age,"min_age":min_age}
print(dict_max_min)


"""
Currently program ends after the check. 
Take the input in while loop and end only if user types "END" for profession
"""

while True:
    profession_1 = input("Enter the profession:")
    if profession_1.upper() == 'END':
        break;
    if (profession_1.lower() in unique_jobs):
        print("Eligible")
    else:
        print("Not Eligible")
        
