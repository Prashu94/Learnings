# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 08:42:14 2016

@author: fractaluser
"""
import datetime
import calendar
from datetime import date
#datetime 

now=datetime.datetime.now()
print(now.strftime("%Y-%m=%d" "%H:%M:%S"))

#take input from the user and prints its area
var_radius=float(input())
print(var_radius**2*3.14)

#take full name of the user and print the full name in reverse order with a spcae between them
first_name=raw_input("Enter first name:")
last_name=raw_input("Enter last name:")
print(last_name +' ' +first_name) 

#Take comma seperated values from user 
#print list and tuple of the values
var_sample=raw_input("Sample Data:")
list = var_sample.split(",")
tuple2=(var_sample)

#take a file input from user and print its extension
var_filename=raw_input("Enter a filename:")
split_filename=var_filename.split('.')
split_filename[-1]

#display the first and the last color in the color list
color_list=[]
for i in range(0,5):
    n=raw_input("Enter Color List:")
    color_list.append(n)
print("First Color:" + color_list[0])
print("Last Color:" +color_list[4])

#calendar output

y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m)) 

#take input from user and print the result as n+nn+nnn
n1=int(input("Enter a number:"))
print(n1+n1**2+n1**3) 

#calculate the number of days between two dates
start_date=date(2011,5,7)
end_date=date(2016,6,12)
date_diff=abs(start_date-end_date)
print(date_diff)

#rerurn the absolute difference for the number in the argument of the function
def func1(x):
    if (x<17):
        return(abs(x-17))
    else:
        return(abs(x-17)*2)
print(func1(3))

#Write a Python program to test whether a number is within 100 of 1000 or 2000
def func2(y):
     return((abs(1000-y)<=100 or abs(2000-y)<=100))
return

#Write a Python program to get a string which is 
#n (non-negative integer) copies of a given string.

#codingbat questions
def front3(str):
  if (len(str)<=1):
    return str
  return(str[0:-1]+str[1:-1]+str[0:-1])
print(front3("Java"))

str2="Chocolate"
str2[0:3]+str2[0:3]+str2[0:3]

str2[len(str2)+1]=str2[len(str2)-1].join('!')

#Write a Python program to get a string 
#which is n (non-negative integer) copies of a given string
def str_func1(str1,n):
    result=" "
    if (n<0):
        return " "
    for i in range(n):
        result=result+str1
    return result      
print(str_func1("abc",2))   

#Write a Python program to find whether a given number (accept from the user)
# is even or odd, print out an appropriate message to the user   
n=int(raw_input("Enter a number:"))
def detect_even_odd(n):
    if (n%2==0):
        return ("The number is even")
    else:
        return("The number is odd")

print(detect_even_odd(n))

#Write a Python program to count the number 4 in a given list.
def count_4_in_list(nums):
    count=0
    for num in nums:
        if (num==4):
            count+=1
    return count
print(count_4_in_list([4,4,5,6,4,4]))   

#didnt understand stall for the moment
#Write a Python program to get the n (non-negative integer) 
#copies of the first 2 characters of a given sting. 
#Return the n copies of the whole string if the length is less than 2 
def substring_copy(str, n):  
  flen = 2  
  if flen > len(str):  
    flen = len(str)  
  substr = str[:flen]  
    
  result = ""  
  for i in range(n):  
    result = result + substr  
  return result  
print(substring_copy("abc",2))

#Write a Python program to test whether a passed letter is a vowel or not
def detect_vowel(str2):
    list5=['a','e','i','o','u','A','E','I','O','U']
    for s in list5:
        if s==str2:
            return("The string is a vowel")
    return("The string is not a vowel")
print(detect_vowel("w"))

#create a histogram from the given list
def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])

#concat all elements of a list into a string
concat_string = lambda l: "".join([str(i) for i in l])
concat_string(['a','b'])

#calculatin gcdd of given numbers
def gcd(x,y):
    gcd=1
    
    if(x%y==0):
        return y
    for k in range(int(x/2),0,-1):
        if (x%k==0) and (y%k==0):
            gcd=k
            break
    return gcd
print(gcd(4,6))

#lcm of numbers
def lcm(x,y):
    if (x>y):
        z=x
    else:
        z=y
    while(True):
        if (z%x==0) and (z%y==0):
            lcm =z
            break
        z+=1
    return lcm
print(lcm(4,6))

#String python practice
string1=raw_input("Enter a string:")
print(len(string1))

#Count the number of characcters in a string
def counter_ex(string2):
    n={}
    for i in string2:
        keys1=n.keys()
        if n in keys1:
            n[i]+=1
        else:
            n[i]=1
    return n
counter_ex("Prashu is my nickname")
        
#Write a Python program to get a string made of the first 2 and the last 2 chars from a given
#a string. If the string length is less than 2, return instead the empty string.

def string_ex(string3):
    if len(string3)>2:
        return(string3[0:2]+string3[-2:])
    else:
        return(string3+string3)
print(string_ex("Prashu")) 


from datetime import datetime
now = datetime.now()

print '%s/%s/%s' % str(now.month,now.date,now.year)