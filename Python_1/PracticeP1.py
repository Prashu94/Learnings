# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 19:20:11 2017

@author: user
"""
#Python Core Datatypes
"""
Numbers
Strings
Lists
Dictionaries
Tuples
Files
Sets
Boolean
Types
Program Unit Types- Functions, Modules, Classes
Implementation-related types- Compiled code, stacktracebacks
"""
import math
#Printing a value in Pyhton
print("Hello World!")
#Data Types
b=True
print(b)

math.pi

#Assigning value to a variable
var_int=9
var_float=9.9 
print(var_int)
print(var_float)

#Operations on numbers
print(11/3.0)#Decimal output
print(11//3.0)#Trancates the decimal value
print(round(11/8,2))

#Strings
str1="Wonder Woman"
str2=","
print(str1+str2)
#Immutability

#Traversing a string
#index starts from 0
str1[0]#First Character of the string
str1[0:3]#From first cahracter tothird character of the string
str1[-1]#Returns the last character of the string
str1[-2]#Returns the second last character of the string
str1[-2:]#Returns from the second last character
#Type Conversions
a='1234'
a1=int(a)
type(a1)

#List
list1=[1,'a',True,2.20]
print(list1)

#Functions used in a list
list2=[2,4,6,7]
list1.append(list2)
list1.extend(list2)

#Sequence Operations on lists
len(list1)
#List comprehensions
#Nested Lists
M=[[1,2,3],
   [4,5,6],
   [7,8,9]
]
M

col2=[row[i] for row in M for i in range(0,3)]
col2

# Add 1 to each item in column 2

col3=[row[1]+1 for row in M]

col3

#Filter out odd items

col4=[row[1] for row in M if row[1]%2 == 0]

# Collect a diagonal from matrix
diag = [M[i][i] for i in range(0,3)]
diag

#Create a generator of row sums

G= (sum(row) for row in M)
next(G)

#Map- Generate results of running items through a function one at a time on request
list(map(sum,M))

#Create a key value for sum as values for keys as the rows
{i : sum(M[i]) for i in range(3)}

#Dictionaries
D= {'food':'Spam','quantity':4,'color':'pink'} 
D#Displays the item in ascending order of keys
D['quantity']+=1

#Creating dictionary from empty dictionary

D1={}
D1['name']='Barry'
D1['Age']=25
D1['Power']='Speedster'

#record the first name and the last name in the above example

D2={}
D2['name']= {'first':'Barry','last':'Allen'}
D2['Age']=25
D2['Power']='Speedster'
D2

#Creating dictionary using dict()

bob1=dict(name ='Bob', job='dev', age = 40)
bob1
bob2=dict(zip(['name','job','age'],['Bob','dev',40]))
bob2

#Sorting keys: for loops

D = {'a' : 1,'b' : 2, 'c' : 3}
D

#Print the keys of the dictionaries
#Onordered key list
Ks = list(D.keys())
Ks

Ks.sort()
#Provides the sorted List 
Ks

#Using loops:

for key in Ks:
    print(key, '=>', D[key])
#Compute the square of list of numbers with the help of comprehensive list function
squares = [x ** 2 for x in range(6)]
squares

#Tuples-Immutable objects
T = (1,2,3,4)
len(T)
#Concatenation in a tuple
T +(5,6)
#Indexing 

T.index(4)
T.count(4)#Frequency of a number in the tuple

#Files objects in python

#Make a new file in output mode
f = open('data.txt','w')
f.write('Hello')#Wirte a strings of character to it
f.write('World')
f.close()

f = open('data.txt','r')
text = f.read()
text

t1=list(text[0:5])
t2=list(text[5:])

list2= t1+t2

#Sets: They are unordered collections of unique and imuutable objects

X = set('spam')
Y = {'h','a','m'}
#A tuple of two set without paranthesis
X,Y
#Intersection
X&Y
#Union
X|Y
#Difference
X-Y

#String Fundamentals

S = ''#Emty String
S1 = "spam's"#Double Quotes, same as single
S2 = 's\np\ta\x00m' #Escape Sequences
S3 = r'\temp\spam' #Raw Strings
B = b'sp\xc4m'#Byte Strings
U = u'sp\u00c4m'#Unicaode String
S1+S2 #Concatenate,repeat

#Files in action
PATH1 = "G:\\extra things\\Knowledge\\practice\\PythonP\\"
myfile = open(PATH1+'Notes.txt','r')
myfile.read()

#Line by Line reading of the file
for line in open(PATH1+'Notes.txt'):
    print(line,end ='')

#Storing python objects in JSON format
name = dict(first = 'Prashant', last = 'Bhat')
rec = dict(name = name, job = ['dev','mgr'],age = 24)

rec

import json

json.dumps(rec)

#Exercises

2**16
2//5#Integer value
2/5.0#Floating value
"spam" + "eggs"

S = "ham"
S * 5#5 times reapeat

"green %s and %s" % ("eggs",S)

'green {0} and {1}'.format('eggs',S) 

('x',)[0]
('x','y')[1]

L = [1,2,3] + [4,5,6]
D = {'x' : 1,'y':2,'z':3}

D['w'] = 0
D['x']+D['w']

#User Defined class in python

class Worker:
    def __init__(self, name, pay): # Initialize when created
        self.name = name # self is the new object
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1] # Split string on blanks
    def giveRaise(self, percent):
            self.pay *= (1.0 + percent)
bob = Worker('Bob Smith', 500000)
bob.lastName()
sue = Worker('Sue Jones', 600000)
sue.lastName()
sue.giveRaise(.10)
sue.pay
###############################################################
#prints the integer cube root, if it exists, of an
#integer. If the input is not a perfect cube, it prints a message to that
#effect.
###############################################################

x= int(raw_input("Enter an integer:"))
ans = 0

while ans**3<abs(x):
    ans = ans + 1;
if ans**3 != abs(x):
    print x, "is not perfect cube"
else:
    if x<0:
        ans = -ans
    print 'Cube root of x is:', ans
#############################################################
#for loop Syntax
#The range function in the line with for is
#evaluated just before the first iteration of the loop, and not reevaluated for
#subsequent iterations.
#############################################################
x=4
for i in range(0,x):        
    print i  
    
#############################################################
x=4
for j in range(0,x):
    for i in range(0,x):
        print i
        x=2
#############################################################        
#implements an algorithm that finds an approximation to
#a square root
#Exhaustive enumaeration method
#############################################################
x=0.25
epsilon = 0.01
step = epsilon ** 2
numgueses = 0
ans = 0.0
#abs(ans **2 -x)>=epsilon this tests whether the difference value of the sqaure root
#is greater than epsilon, 
while (abs(ans **2 -x)>=epsilon and ans <=x):
    ans +=step
    numgueses +=1
print 'numgueses= ', numgueses
if abs(ans**2 - x) >= epsilon:
    print 'Failed on square root of', x
else:
    print ans, 'is close to square root of', x
###########################################################
#Enhanced Algorithm
#Bisection Serach
###########################################################
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print 'low =', low, 'high =', high, 'ans =', ans
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to square root of', x
########################################################
#Newton Rhapson method
########################################################
epsilon = 0.01
k = 245.0
numGuesses=0
guess = k/2.0
while abs(guess**2 - k) >= epsilon:
    numGuesses+=1    
    guess = guess - (((guess**2) - k)/(2*guess))
print 'Square root of',k,'is about', guess
print 'Number of guesses',numGuesses
######################################################
#Function and SCoping
######################################################
"""
Syntax of function
def name of function (list of parameters):
    body of function
def max(x,y):
    if x>y:
        return x
    else
        return y
"""
"""
The function printName assumes that firstName and
lastName are strings and that reverse is a Boolean. If reverse == True, it prints
lastName, firstName, otherwise it prints firstName lastName.
"""

#########################################################
def printName(firstName,lastName, reverse):
    if reverse:
        print lastName +' '+ firstName
    else:
        print firstName+' '+lastName
firstName= raw_input("Enter First Name:")
lastName= raw_input("Enter Last Name:")
reverse= raw_input("Want reverse:")

printName(firstName,lastName,reverse)

#########################################################
"""
Finding an approximation to a root
"""
#########################################################

def findRoot(x,power,epsilon):
    if x<0 and power%2 ==0:
        return None
    low=min(-1.0,x)
    high=max(1.0,x)
    
    ans=(low+high)/2.0
    
    while abs(ans**power-x)>=epsilon:
        if ans**power <x:
            low=ans
        else:
            high=ans
        ans=(low+high)/2.0
    return ans

def testFindRoots():
    epsilon= 0.0001
    for x in (-0.25,0.25,2,-2,8,-8):
        for power in range(1,4):
            print 'Testing x =' +str(x) +\
                  ' and power =' +str(power)
            result = findRoot(x,power,epsilon)
            if result == None:
                print 'No root'
            else:
                print '  ',result**power,'~=',x
testFindRoots()
############################################################
#Recursion in python
############################################################
#Factorial Example
#Iterative
def factI(x):
    """Assumes x is an int >0 
    Returns x!"""
    result = 1
    
    while x > 1:
        result = result * x
        x-=1
    return result
#REcursive
def factR(x):
    """Assumes x is an int >0 
        Returns x!"""
        
    if x==1:
        return 1
    else:
        return x * factR(x-1)
##########################################################
#Print the dimensions of a cuboid,
#input x,y,z,n

x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
n = int(raw_input())

ar=[]
p=0
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i+j+k) != n:
                ar.append([])
                ar[p] = [ i , j , k ]
                p+=1
print ar

x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
n = int(raw_input())

list_1 = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=1]
print list_1

x,y,z,n = [input() for i in range(4)]
print [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
###################################################################################
#HackerRank
###################################################################################
#You are given n numbers. Store them in a list and find the second largest number.

i = int(input())
lis = list(map(int,raw_input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print max(lis)

###################################################################################
#Given the names and grades for each student in a Physics class of N students, 
#store them in a 
#nested list and print the name(s) of any student(s) having the second lowest grade.
####################################################################################

marksheet =[]
for _ in range(0, int(input())):
    marksheet.append([input(), float (input())])
second_highest = sorted(list(set(marks for name, marks in marksheet)))
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))


##############################################################################
#import numpy
##############################################################################

import numpy as np

data1 = [6.5,4,5.5,6]

#creating an array using numpy
arr1 = np.array(data1)

#Nested Sequences, like a list of equal lengths wil be converted into multidimensional array
data2 = [[1,2,3,4],[5,6,7,8]]

#creating multi dimensioanl
arr2d = np.array(data2)


arr2d.ndim

arr2d.shape

#Slicing the array

arr2d[0,1]

arr2d[:2,1]#2 values of second column

arr2d[:2,0]#2 values of first column

arr2d[1,:2]#2 values of second row

arr2d[0,:3]#3Values of first row

arr3d = np.array([[1,2,3],[4,5,6],[7,8,9]])

arr3d.ndim

arr3d.shape


old_Values = arr3d[0].copy()

arr3d[0] = 10

#Fancy Indexing using for loops

arr = np.empty((8,4))

for i in range(8):
    arr[i]=i
arr

arr = np.arange(15).reshape((3,5))

arr
#Transposing an array
arr.T

#While doing matrix computations
#we do XT . X using np.dot

arr = np.random.randn(6,3)

#Dot product of two matrix
np.dot(arr.T,arr)

#For higher dimensional arrays, transpose will accept a tuple of axis numbers 
#to permute the axes

#Creates an arraystack
arr =np.arange(16).reshape((2,2,4))



arr.transpose((1,0,2))

#Data Processing using Arrays

#Example: sqrt(x**2+y**2)

#1000 equally spaced points
points = np.arange(-5,5,0.01)

#takes two 1D arrays and produces two 2D matrices corresponding to (x,y) values
xs,ys = np.meshgrid(points,points)

xs
ys

import matplotlib.pyplot as plt

z = np.sqrt(xs**2 + ys**2)

z

plt.imshow(z,cmap = plt.cm.gray);
plt.colorbar

plt.title("Image plot of $\sqrt{x^2+y^2}$ for a grid of values");

#Creates an array of 10 0's
np.zeros(10)

np.zeros((3,6))

#Returns an ndarray
np.arange(15)


################
import turtle

turtle.showturtle()

turtle.write("Welcome to Python")

