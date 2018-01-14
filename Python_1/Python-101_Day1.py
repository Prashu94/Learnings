# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:30:26 2016

@author: fractaluser
"""

print("Hello World!")

#Boolean

b=True
print(b)

bool(1)
bool(0)

#Numbers
a=22
print(a/7)
print(a/7.0)
print(round(a/7.0,2))

#Strings
string1='Hi my name is Sujit'
ss='.'
print(string1+ss)

#Type Conversions
a='1234'     #string
int(a)       #Conversion 

#(Note: Conversion is temporary and limited to execution of that statement itself)
print(a+1)
print(int(a)+1) #Confirming conversion (convert and print in one statement itself)

#List
lis1=[1,2,3,4,5,6,7,8,9]
print(lis1)

lis1.append('Fractal')

lis1.insert(9,'Analyst')
lis1.insert(10,'@')

#Printing lists
lis1[1]                   #prints value on index 1
lis1[:-1]                 #prints whole list except last element
lis1[1:4]                 #prints elements from index 1 to index (4-1)
lis1[:4]                  #prints elements from index 0 to index (4-1)
lis1[::-1]                #prints list from last index stepping by 1
lis1[::2]                 #Prints elemnents from index 0 till last index stepping by 2
lis1[10]='at'             #Updating value at index 10
lis1.append([4,3,2,1])    #adding list as an element in a list
lis1                      #print list
lis1[-1][1]=10            #accessing innner list and updating it
lis1[-1].append('0')      #Adding string in inner list

#Tuples
tup1=tuple(lis1)        #tuple can be converted to,list and vice versa

tup2=(1,2,4)            #creating a tuple
tup2[0]=3               #cant append/edit tuple

#Sets
set1={1,2,3,4,''}
set2={3,4}

set2-set1

list(set1-set2)         #we can convert set to list to edit it and convert it back to set

#Dictionary

dic1={'hi':'Sujit','flower':'floral','hello':'hey'}
dic1
#in above example, linking of elements of dictionary took place
#'hi' was a key. when it was assigned as value to another key, it gave its own
#value to the caller key

dic2= {'Sujit':{'Age':22,'Sex':'M'},'Raj':{'Age':24,'Sex':'M'}}
dic2                    #dictionary of dictionaries
dic2['Raj']['Sex']      #selective printing

#Spliting/Joining a String
str3='Hello guys welcome to the first session of python'

str_split = str3.split(' ')

'-'.join(str_split)

list(str3)              #converts into list by taking each letter as one element

#Python Map
list(map(str,lis1))     #convert each value of list into string

lis3=list(range(2004,2020))

#Exercise: print 'select * fromm table where year=2004 or 2005...'
str_exer='Select * from table where year = '+' or year = '.join(map(str,lis3))
str_exer

#Checking Type
type(2012)
type(str_exer)
