# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 11:42:25 2016

@author: fractaluser
"""
import math
#from __future__ import division
print("Hello World!")

#datatypes
a=2
print(a)
print(type(a))

#checks the instance of the value 
#to find if it is of the type integer
isinstance(2.0,int)
isinstance(2.0,float)


#converting an object/value to a certain type
a1="1"
print(type(int(a1)))
float(2)
bool(10)
isinstance(1,bool)
#this is an empty string ie equivalent to zero
str1=""
bool('' )#false
bool(' ')#true


#Math Operations(+,*,-,**,/,%,//)
#exponent of values
print(10^2)
print(10/3)#gives float value in console(true division)
print(10//3)#it gives integer value in console(floor division)
print(-10/4)#in this it gives -3 (lower value)


#Boolean operators and comparison
print(3>2)
x=5
print(x>=3)
print(5>3 or 5<3)

print(False or not False and True)#unary operation will be performed first 

#conditional statements

if x>0:
    print("positive")
#multiple condition checks
if x>0:
    print('Greter than zero')
elif(x==0):
    print("Equal to zero")
if(isinstance(x,int)):
    print("Integer variable")

#if else in a single line
'positive' if x>0 else 'negative'

print 'str'+'0'
3+2.5


#Exercises:
#1.
i=0
s1="34"
s1="abv34"
if isinstance(float(s1),float):
    print(float(s1)**2)      

a=1
b=2
c=4
d=b**2-4*a*c
if d > 0:
    rootsminus=(-b+math.sqrt(d))/2*a
    rootsplus=(-b-math.sqrt(d))/2*a
    print("Two real roots:",rootsminus,rootsplus)
elif d==0:
    rootsminus=(-b+math.sqrt(d))/2*a
    rootsplus=(-b-math.sqrt(d))/2*a
    print("Equal Roots:",rootsminus,rootsplus)
else:
    print("Imaginary roots")


#Lists,Tuples
#List
#looping (for,while)
x_list=[3,4,5,6]
#range returns a list of all the indexes
#range(1,10) -the first parameter is inclusive and the second parameter is exclusive
#if you just give x_list we get the actual elements list
#range(1,10,2)-third parameter is the step function
for element in range(len(x_list)):
    print element, x_list[element]

i=0
while i<len(x_list):
    print i,x_list[i]
    i+=1
    
#Exercise2:Wriet a program which take numbers from 200 till 
#3000 and print all those divisible by 7 but not by 5 or they are divisible by 3

for i in range(2000,3000):
    if(i%7==0 and i%5!=0 or i%3==0):
        print i

#break keyword will help to break out of the existing loop
#use break keyword only in for loop only
for i in range(10):
    if i==5:
        break;
    
    print i
    
#loop break
for i in range(20):
    print "Value in outer loop:",i
    
    for j in range(10):
        
        if j==5:
            break;
        print "Value in inner loop:",j

for i in range(10):
    if i<5:
        pass
    print i        

#creating an empty list
empty_list=[]
empty_list=list() 
len(empty_list)   
#Creating a list
flash=['Barry','Cisco','Wally']
#appending a list
flash.append('Iris')
flash.extend(['The Flash','t'])
flash.remove('The Flash')
flash[2]='Catelyn'
flash.insert(2,'Joe')
#pop removes element by index number(returns the element)
flash.pop(3)

#concatenating the list with a plus
flash=flash +[['Joe','James','Oliver']]
flash[3][1]
flash.remove(['Joe','James','Oliver'])
#counting a particualr element in the list
#flash.count('Joe')

#.index function with list
flash.index('Joe')

#List SLiciing
weekdays=['mon','tue','wed','thu','fri','sat','sun']
#elements o inclusive 3 exclusive
weekdays[0:4]
#elements starting from 4th to end
weekdays[3:]
#every second element i.e skips the alternate element
weekdays[1::3]
#reversing a list i.e it prints the list in the reverse order
weekdays[::-1]
weekdays[-1]
#Sorting the list
flash.sort()
flash.sort(reverse=True)
#sorting the list with the help of the string
flash.sort(key=len,reverse=True)
#ascii character ord function
#reverse of ord function it is chr function
chr(45)
ord('A')

#sorted fuction
dc=sorted(flash,reverse=True,key=len)

#Exercise 3:
#hints
range(4)[1:]

#Day3:
#Tuples

#ordered,iterable,immutable,can contain multiple data types
#order is maintained in the list
digits=(2,3,4,'two',True)

#create a tuple from the list
digits=([1,2,3],)

#trailing comma is required to indicate it is a tuple
#if we do not put a comma it is considered as a a normal integer
zero=(0)
zero=(0,)

#.count()-counts the number of elements in the list
#.index()-returns the postion of the particular number in the tuple
#cannot cahnge the elements of the tuple
digits[2]=2

#concatenatinating tuples
#tuples douse not append values to itself
digits=digits+(3,4)
#digits.append() not available 

#duplicating tuples
(3,4)*2
(1,)*10

#sort a list of tuples
tens=[(2,3),(1,1),(7,10)]
sorted(tens)

#unpacking the value of tuple
bart=('male',10,'simpsons')
(sex,age,surname)=bart

print sex

#Strings
#convert another datatye in  strings
s=42
s1=str(s)
s1[0]

#string slicing is like list slicing
#length function is also available
#0:2 values of the string
s1[:1]
#Basic string methods
s1="Prashu is great"
s1.lower()
s1.startswith('P')
s1.endswith('t')
s.isdigit()
s1.find('t')
s2=s1.replace("Prashu","Prashant Bhat")
s2.split()
#join or concatenate a string

flash=['barry','wally','Jesse']
' '.join(flash)

#concatenating the string

#REmove whitspace from the start or the end of the string
flash1='Barry is the flash'
flash1.split()

#formatting the string(old way)
#see it on the internet
print 'First %s line\nSecond %s  Line '%(1,2)
print('dvfsmn\ndfsg')
print(r'first line\nfirst line')

#Dictionary
#unordered,iterable,mutable,can contain multiple datatypes
#made of key value pairs

#create an empty dictionary
empty_dict={}
empty_dict=dict()
print empty_dict

#creating dictionary with value
flash_family={'The Flash':'Barry','Age':'25','Sex':'M'}
flash_family['The Flash']
#the no. of key value pairs
len(flash_family)
#check if the key exists in the dictionary
'Age' in flash_family

#all the keys of the dictionary
flash_family.keys()

#all the values of the dictionary
flash_family.values()

#to get the tuple of the list
flash_family.items()

#adding the new entry to the dictionary
#it adds the new thing as a new key value pair
flash_family['speed']='3 mach'

#dictionary value can be a list
flash_family['friends']=['Joe','Joe']
flash_family['friends1']='joe'
#multiple key value pairs 
#,update(('':'','':''))

flash_family.get('Adversary','not found')
flash_family['friends'][0]
flash_family['friends'].remove('Joe')

'best friend of the flash is %(friends)s'%flash_family

#Sets
#unordered,iterable,mutable
#made of unique elements
#similar to dictionaries but without any values
#creating an empty sets
empty_set=set()

#create a set directly
lang={'Java','Python','R','Java'}

#create a set from the list
snake=set(['cobra','viper','Python'])

'Python' in lang

#Set operations
#intersections
lang & snake

#union
lang | snake

#modifying a set
lang.add('sql')
lang.add('pyhton')


#remove an element
lang.clear()


#add multiple elements 
lang.update(['C','SQL'])

#sorting a set
#by defualt it is ascending
sorted(lang)



#day 04
def print_this(x):
    return x**2

def cube_f(x):
    return x**3

#define a function with two positional arguments and one keyword arguments
def calc (a,b,op='add'):
    if op=='add':
        return a+b
    elif op=='sub':
        return a-b
    else:
        return "Addition subtraction"
calc(2,3)
#Anonymous function(lambda)
squared1=lambda x:x**2
squared1(3)

#List comprehensions
nums=[1,2,3,4]
cube=[num**3 for num in nums]

input1 = "Tesla’s acquisition of SolarCity officially closed Monday morning, bringing together Elon Musk’s electric vehicle company with the solar energy company founded by his cousins Lyndon and Peter Rive. It’s a long-term investment with no real short-term payoff, and both Tesla and SolarCity will need a lot of cash to stay operational until this deal starts to bear fruit."

input2 = "As expected, Tesla completed its $2.6 billion acquisition of SolarCity, a company spokesperson confirmed Monday. The deal unites two of Elon Musk’s companies, enabling the billionaire to sell both electric cars and solar roofs to his customers under one corporate brand.Tesla’s recent solar roof tile launch showed why Musk believes the companies are a natural fit under a unified Tesla roof"


input1=input1.lower()
input2=input2.lower()

input1=input1.split(' ')
input2=input2.split(' ')

common = set(input1).intersection( set(input2) )

common1=list(common)

for n in range(len(common1)):
    if (len(common1[n])>=3):
        print(common1[n])

