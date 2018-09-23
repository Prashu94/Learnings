# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 21:14:03 2018

@author: Prashant Bhat
"""
import re
import pandas as pd
class CustomerClass():
    def __init__(self,fullname):
        self.full = fullname
        s = self.full.split()
        self.last_name = ''
        for l in s:
            if(len(l)==2):
                try:
                    find = re.compile(r'^([^.]*).*')
                    self.title = re.search(find,s[0].strip()).group(0)
                    self.first_name = s[1]
                finally:
                    pass        
            else:
                try:
                    find = re.compile(r'^([^.]*).*')
                    self.title = re.search(find,s[0].strip()).group(0)
                    self.first_name = s[1]

                finally:
                    pass        
path = "G:\\extra things\\Knowledge\\practice\\Edureka\\Module3\\"
customer_data = pd.read_csv(path+"FairDealCustomerData.csv",names = ['Brand','Name','Status'])
customer_data.head()
customer_data.tail()
list_data = list(customer_data['Name'])
for fullname in list_data:
    name = CustomerClass(fullname)
    title = name.title
    first_name= name.first_name
    last_name= name.last_name
    print("Title:",title)
    print("First_Name:",first_name)
    print("Last_Name:",last_name)

