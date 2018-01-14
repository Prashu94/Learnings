# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:49:18 2016

@author: fractaluser
"""
import datetime
import math
import re
print("Hello World")
#Data Types in Python
#Boolean
b=True
print(b)

var_int=9
var_float=9.9
print(var_int)
print(var_float)

#operations on numbers
print(11/3.0)
print(11//3.0)
print(round(11/8,2))

#Strings
str1="My name is Prashant Bhat"
str2="."
print(str1+str2)
str1[1:]
#Type Conversions
a='1234'
int(a)

#list
list1=[1,'a',True,2.2]
print(list1)
list1
#functions of list
list2=[2,4,6,7]
list1.append([1,2,3,4])
list1.extend(list2)

#subsetting list list1[1:4]
list1[1]                   #prints value on index 1
list1[:-1]                 #prints whole list except last element
list1[1:4]                 #prints elements from index 1 to index (4-1)
list1[:4]                  #prints elements from index 0 to index (4-1)
list1[::-1]                #prints list from last index stepping by 1
list1[::2]                 #Prints elemnents from index 0 till last index stepping by 2
list1[3]='at'             #Updating value at index 
list1.append([4,3,2,1])    #adding list as an element in a list
list1                      #print list
list1[-1][1]=10            #accessing innner list and updating it
list1[-1].append('0')      #Adding string in inner list

#Tuples
tup1=tuple(list1)        #tuple can be converted to,list and vice versa

tup2=(1,2,4)            #creating a tuple
tup2[0]=3               #cant append/edit tuple

#Sets
set1={1,2,3,4,''}
set2={3,4}

set2-set1

list(set1-set2)         #we can convert set to list to edit it and convert it back to set

#Dictionary

dic1={'Oliver':'Arrow','Felicity':'Overwatch','Barry':'Flash'}
dic1
#in above example, linking of elements of dictionary took place
#here Oliver is the key and Arrow is the value for the key
#to access the value of the dictionary we can use the key of the dictionary 
#dictionary key can have more than one values in the curly braces 
#to access the values inside the second curly brace we can use double indesxing 
#in python double indexing takes place with the help of two'[][]'
dic2= {'Oliver':{'Age':22,'Sex':'M'},'Barry':{'Age':24,'Sex':'M'},'Felicity':{'Age':23,'Sex':'F'}}
dic2                    #dictionary of dictionaries
dic2['Oliver']['Age']      #selective printing

#Spliting/Joining a String
str3='Hello guys welcome to the first session of python'

str_split = str3.split(' ')

' '.join(str_split)

list(str3)              #converts into list by taking each letter as one element

#Python Map
list1=list(map(str,list1))     #convert each value of list into string but does not save it to the memeory 
#i.e map() just convert the list innto string fro representation 
#but whene you access the type of the list next time you get the previous type and not the converted type


lis3=list(range(2004,2020))

#Exercise: print 'select * fromm table where year=2004 or 2005...'
str_exer='Select * from table where year = '+' or year = '.join(map(str,lis3))
str_exer

#Checking Type
type(2012)
type(str_exer)

#DAY 02
#Dictionary joining

dic2= {'Name':'Oliver','Age':22,'Sex':'M'}
dic2
dic1.keys()
dic1.values()
type(dic1.keys())
#Get the output as 'Age-Name-Sex -- 24-Aditya-M'
#first all the keys are printedd with - as join 
#second the values are converted to string to bring uniformity and then values are printed
'-'.join(dic2.keys())+' -- '.join(map(str,dic2.values())) 

#For loop
list3=range(10)
list3[0]
list3[1]
for number in list3:
    print(number)
    
#for printing the index an the value
for index in range(len(list3)):
    print(index)
    print(list1[index])
    
#print the values of dictionary using loop
for i in dic2:
    print i,dic2[i]

#fro printing only the values of the dictionary
#if you only want to print the values of the ddictionary specify
#.values()
for i in dic2.values():
    print(i)

#if else loop in for loop
for index in range(len(list3)):
    if index<5:
        print(index)
        print(list3[index])
  #  elif index==5
 #       print('last one')
  #  else:
   #     break

for index in range(len(list3)):
    if index==5:
        print(index)
        print(list3[index])
    else:
        pass
#while loop
i=0
while(i<=5):
    if(i%2==0):
        print(i)
    i+=1

#function definition in python'
#can take anything as an input and return anything as an output
def func(list3):
    return(list3)
print(func(list3))

#in this the lopp is traversing the values of list3 not the indexes
def sfunc(list3):
    ret_list=[]
    for i in list3:
        ret_list.append(i**2)
    return ret_list

n=int(input())
year_list=[]
for i in range(n,n+5):
    year_list.append(i)
print(year_list)
#comprehensive list method to return a list from the function
list_compre=[i for i in range(1,10)]
def func_alt(list1):
    return[num**2 for num in list1 if (num%5==0)]
func_alt([2,4,5,8,7])

def square1(x):
    return x**2
list(map(square1,list_compre))

#Exercise : To create alist of lists using list comprehension
list_compre1=[[i for i in range(j-10,j)] for j in range(10,100,10)]
#Exercise :Print Prime Numbers in a range of 1 to 10 using list comprehension
list_compre2=[i for i in range(2,20) if all(i%j!=0 for j in range(2,i)) ]

#operators
#lambda : an alternative to function
f=lambda x: x**2
f(10)

f1=lambda x,y,z:x*y*z
f1(4,3,2)


list(map(lambda x:x**2,list_compre))

f2=lambda x:[i**2 for i in x]
map(f2,list_compre1)

if 9 in list_compre:
    print('Yes')
    
def func_gen(x):
    for i in x:
        if (i%10==0):
            yield i
a =func_gen(range(10000))
next(a)

for i in a:
    if  (i>200):
        break

for i in a:
    pass

#file reaading
file_read=open('/home/fractaluser/Desktop/practice.txt','r')
txt=file_read.read()
lines=txt.split('\n')

#day03
#math function
math.pow(10,2)
math.sin(math.pi/3)
#if you want specific function from math package you can use this shown below
from math import pow
pow(10,2)

#giving alias to the imported package
import numpy as np
np.array([1,2,3,4])
string1="Hello Prashu this is my last@#$%^day of python 101, so i am trying my best to learn and complete this course"
re.sub('[^a-zA-Z]','',string1)


f1=open('/home/fractaluser/Desktop/learning/Python/word_freq_ini.txt','r')
txt1=f1.read()
f1.close()
txt1=txt1.lower()
txt2=re.sub('[^a-z]','',txt1)
from collections import Counter
cnt=Counter(txt2)

import matplotlib.pyplot as plt
plt.bar(range(len(cnt)),cnt.values(),align='center')
plt.xticks(range(len(cnt)),cnt.keys())
plt.show()

#sorted keyword arranges the list in a particular order
sorted([5,2,9,3])
sorted(cnt.keys())
sorted(list(zip(cnt.keys(),cnt.values())),key=lambda x:x[0])
#() direct samjah ki yeh ek tuple hai
list1=[(i,cnt[i]) for i in sorted(cnt.keys())] 
[x[1] for x in list1]
list(map(lambda x:x[1],list1))

plt.bar(range(len(cnt)),[x[1] for x in list1],align='center')
plt.xticks(range(len(cnt)),[x[0] for x in list1])
plt.show()

#ord
ord('b')

f2=open('/home/fractaluser/Desktop/learning/Python/analyse.txt','r')
txt=f2.read()
f2.close()
txt3=txt.lower()
txt4=re.sub('[^a-z]','',txt3)

from collections import Counter
cnt1=Counter(txt4)

import matplotlib.pyplot as plt
plt.bar(range(len(cnt1)),cnt1.values(),align='center')
plt.xticks(range(len(cnt1)),cnt1.keys())
plt.show()

sorted(cnt.keys())
sorted(cnt.values())
sorted(cnt1.keys())
sorted(cnt1.values())

list1=[(i,cnt[i]) for i in sorted(cnt.keys())]
list2=[(i,cnt1[i]) for i in sorted(cnt.keys())]
cnt2=cnt-cnt1

    
list3=[(i,cnt2[i]) for i in sorted(cnt2.keys())]
#list4=[(i,cnt3[i]) for i in sorted(cnt3.keys())]

plt.bar(range(len(cnt2)),[x[1] for x in list3],align='center')
plt.xticks(range(len(cnt2)),[x[0] for x in list3])
plt.show()

#plt.bar(range(len(cnt3)),[x[1] for x in list3],align='center')
#plt.xticks(range(len(cnt3)),[x[0] for x in list3])
#plt.show()

txtout=''
for letter in txt4:
    txtout+=chr(ord(letter)-7)

ord('c')
chr(ord('c'))