# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 17:22:34 2018

@author: Prashant Bhat
"""
import os 

newfile = open("Edureka_Py.txt","w+")

for i in range(1,10):
    newfile.write("\n Hello, welcome to Python:")
for i in range(1,10):
    print(newfile.read())

newfile.seek(0)
print(newfile.tell())

os.rename("Edureka_Py.txt","Edureka.txt")
##os.remove("Edureka_Py.txt")
newfile.close()

#############################################################################
list1 =["Marketing","Content Designing","Sales"]
print(list1)

#Concatenation
print(list1+["Python""Hadoop"])
#Repetition
print(list1*2)
#Membership Testing
print('Marketing' in list1)
#Indexing
print(list1[2])
#Slicing
print(list1[0:2])

#A Tuple inside a list

list2 =[(1,2,3),("Python","Java")]
print(list2[1][0:1])

