# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 21:14:25 2018

@author: Prashant Bhat
"""

"""
1.A Robot moves in a Plane starting from the origin point (0,0). 
The robot can move toward UP, DOWN, LEFT, RIGHT. 
The trace of Robot movement is as given following:
UP 5DOWN 3LEFT 3RIGHT 2The numbers after directions are steps.  
Write a program to compute the distance current position after sequence of movements
"""

pos = {"x":0,"y":0}

while True:
    line = input()
    if not line :
        break
    direction,steps =  line.split()
    if direction == 'UP':
        pos["y"]+=int(steps)
    elif direction == 'DOWN':
        pos["y"]-=int(steps)
    elif direction == 'RIGHT':
        pos["x"]+=int(steps)
    elif direction =='LEFT':
        pos["x"]-=int(steps)
print(int((int(pos["x"])**2+int(pos["y"])**2)**0.5 ))

"""
2.Data of XYZ company is stored in sorted list. 
Write a program for searching specific data from that list.
"""
data_xyz = {"Founded":1984,"City":"Mumbai","Employee_Strength":1000}
data_to_find = input("Enter the data you need to find about the country: ")
if (data_to_find == data_xyz.keys()):
    print(data_xyz.values())

"""
3.Weather forecasting organization wants to show is it day or night.
So, write a program for such organization to findwhether is it dark outside or not.
"""
import time
localtime = time.localtime(time.time())
if (localtime.tm_hour > 12):
    print("Night")
else:
    print("Day")
    
"""
4.Write a program to find distancebetween two locations when their latitude and longitudes are given.
"""
from math import radians, sin, cos, acos
print ("Input coordinates of two points:")
slat =radians(float(input("Starting Latitude: "))) 
slon =radians(float(input("Starting Longitude: ")))
elat =radians(float(input("Ending Latitude: "))) 
elon =radians(float(input("Ending Longitude: ")))

dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
print("Distance is %.2fkm "%dist)

"""
6.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
 between 2000 and 3200 (both included). 
 The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
sequence = list(range(2000,3201))
output_print = []
for i in range(len(sequence)):
    if (sequence[i] % 7 ==0 and sequence[i] % 5 !=0):
        output_print.append(sequence[i])
print (output_print)

"""
7.Write a program which can compute the factorial of a given numbers. Use recursion to find it.
"""
def factorial(n):
    if (n <=1 ):
        return 1
    else:
        return(n*factorial(n-1))
number1 = int(input("Enter the number: "))
print ("Factorial of the number is:",factorial(number1))

"""
8.Write a program that calculates and prints the value according to the given formula:
    Q = Square root of [(2 * C * D)/H]Following are the fixed values of C and H: C is 50. H is 30.
    D  is  the  variable  whose  values  should  be  input  to  
    your  program  in  a  comma-separated sequence.
"""

import math
c = 50
h = 30
value = []
items = [x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print (','.join(value))

"""
9.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡-Y-1.
"""
row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)


"""
10.Write a program that accepts a comma separated sequence of words as input 
and prints the words in a comma-separated sequence after sorting them alphabetically.
"""

no_input1 = int(input())
word_list =list(input().rstrip().split(','))[:no_input1]
print(','.join(sorted(word_list)))

"""
11.Write a program that accepts sequence of lines as input 
and prints the lines after making all characters in the sentence capitalized. 
"""
lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break;

for l in lines:
    print(l)
    
"""
12.Write a program that accepts a sequence of whitespace separated words as input and   prints   the   words   
after   removing   all   duplicate   words   and   sorting   them alphanumerically.
"""

no_input2 = int(input())
word_list2 =list(input().rstrip().split())[:no_input2]
tup1 = tuple(word_list2)
print(' '.join(sorted(tup1)))

"""
13.Write  a  program  which  accepts  a  sequence  of  comma  separated  4  
digit  binary numbers  as  its  input  and  then  check  whether  
they  are  divisible  by  5  or  not.  The numbers that are divisible by 5 are 
to be printed in a comma separated sequence.
"""

items = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p, 2)
    if not x%5:
        items.append(p)
print(','.join(items))

"""
14.Write  a  program  that  accepts  a  sentence  
and  calculate  the  number  of  upper  case letters and lower case letters
"""

def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brow Fox')

"""
15.Give example of fsum and sum function of math library.
"""

#FSum-finds sum of range or an iterable
import math
print(math.fsum(range(10)))

#Sum- finds the sum of list of  numbers
numbers =[1,2,3,4,5]
sum1 = sum(numbers)
print(sum1)
