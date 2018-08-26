# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 22:54:39 2018

@author: Prashant Bhat
"""
"""
Case Study I

"""
"""
1.Write a program which will find factors of given number and find either the factor is even or odd
"""

#Take a number as input from the user
number = int(input())
i = 1
factors = []
while i<=number:
    if (number%i==0):
        factors.append(i)
    i=i+1
#Prints all the factors of the number given as input
        
print(factors)
even_odd=[]
for j in range(len(factors)):
    if (factors[j]%2==0):
        even_odd.append('Even')
    else:
        even_odd.append('Odd')
print(even_odd)

"""
2.Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically. 
"""

seq_string = input()
print(''.join(sorted(seq_string)))

"""
3.Write a program, whichwill find all the numbers between 1000 and 3000 (both included) such that each digit of a number is an even number. The numbers obtained should be printed in a comma separated sequence on a single line.
"""

sequence = list(range(1000,3001))
output_print = []
for i in range(len(sequence)):
    if (sequence[i]%2==0):
        output_print.append(sequence[i])
print (output_print)


"""
4.Write a program that accepts a sentence and calculate the number of letters and digits.
"""

str_in = input()
digits=letters=0

for c in str_in:
    if c.isdigit():
        digits+=1
    elif c.isalpha():
        letters+=1
    else:
        pass
print ("Letter:",letters)
print ("Digits:",digits)


"""
5.Design a code which will find the given number is Palindrome number or not.
"""

num = input('Enter any number : ')
try:
    val = int(num)
    if num == str(num)[::-1]:
        print('The given number is a PALINDROME')
    else:
        print('The given number is NOT a palindrome')
except ValueError:
    print("That's not a valid number, Try Again !")


"""
6.What is the output of the following code?
nums =set([1,1,2,3,3,3,4,4])
print(len(nums))

Answer: 4
Explanation:
    As sets consists of only unique elements, hence the above set will consists of nums ={1,2,3,4}
    and the length for the same is 4
"""

"""
7.What will be the output?
d ={"john":40, "peter":45}
print(list(d.keys()))

Answer: ['john','peter']

Explanation:
    d is a dictionary containing keys as "john" and "peter" and values 40 and 45
    d.keys()- prints the keys in the dictionary which is "john" and "peter"
        
"""

"""
8.A website requires a user to input username and password to register. 
Write a program to check the validity of password given by user. 
Following are the criteria for checking password:
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    1. At least 1 letter between [A-Z]
    3. At least 1 character from [$#@]
    4. Minimum length of transaction password: 6
    5. Maximum length of transaction password: 12
"""
import re
password = input("Enter a password:")
x = True
while x:
    if (len(password) <6 or len(password) >12):
        break
    elif not re.search("[a-z]",password):
        break
    elif not re.search("[0-9]",password):
        break
    elif not re.search("[A-Z]",password):
        break
    elif not re.search("[$#@]",password):
        break
    elif re.search("\s",password):
        break
    else:
        print("Valid Password")
        x=False
        break
    if x:
        print("Not a Valid Password")
"""
9.Write a for loop that prints all elements of a list and their position in the list.
a = [4,7,3,2,5,9] 
"""
a = [4,7,3,2,5,9]
for index,val in enumerate(a):
    print("Index:",index,"Values:",val)

"""
10.Please   write   a   program   which   accepts  a   string   from   console   and   
print   the characters that have even indexes.
"""

string1 = input("Enter a string:")
l_string =[]
for i in range(len(string1)):
    if(i%2 == 0):
        l_string.append(string1[i])
print(''.join(l_string))

"""
11.Please write a program which accepts a string from console andprint it in reverse order.
"""

string2 = input("Enter a string:")
string2[::-1]

"""
12.Please write a program which count and print the numbers of each character in a string input by console.
"""

string3 = input("Enter a string:")

for i in range(len(string3)):
    print(string3[i],',',string3.count(string3[i],0,len(string3)))

"""
13.With   two   given   lists   [1,3,6,78,35,55]   and   [12,24,35,24,88,120,155],   
write   a program to make a list whose elements are intersection of the above given lists.
"""

list1= [1,3,6,78,35,55]
list2= [12,24,35,24,88,120,155]

set1 = set(list1)
set2 = set(list2)
print(set1&set2)


"""
14.With a given list [12,24,35,24,88,120,155,88,120,155], 
write a program to print this list after removing all duplicate values with original order reserved.
"""
def removeDuplicates(list3):
    new_list =[]
    seen = set()
    
    for i in list3:
        if i not in seen:
            seen.add(i)
            new_list.append(i)
    return new_list
list3 = [12,24,35,24,88,120,155,88,120,155]
print(removeDuplicates(list3))

"""
15.By using list comprehension, please write a program to print the list 
after removing the value 24 in [12,24,35,24,88,120,155].
"""
print ([x for x in [12,24,35,24,88,120,155] if x!=24 ])

"""
16.By using list comprehension, please write a program to print the list after 
removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
"""

print([x for index,x in enumerate([12,24,35,70,88,120,155]) if index not in [0,4,5]])

"""
17.By using list comprehension, please write a program to print 
the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
"""
print ([x for x in [12,24,35,70,88,120,155] if (x%5==0 and x%7 ==0)])

"""
18.Please  write  a  program  to  randomly  generate  a  list  with  5  numbers,  
which  are divisible by 5 and 7 , between 1 and 1000 inclusive.
"""


list4 =[]

for x in range(1,1001):
    if (x%5 == 0 and x%7 ==0):
        list4.append(str(x))
print(','.join(list4[0:4]))


"""
19.Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0).
"""

terms = int(input("Enter the number of terms:"))
sum1=0
for i in range(1,terms+1):
    sum1= sum1 + float(i)/(i+1)
    i = i+1 
print(sum1)
