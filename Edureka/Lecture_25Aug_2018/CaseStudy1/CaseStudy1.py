# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 14:03:16 2018

@author: Prashant
"""

"""
Case Study1:
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