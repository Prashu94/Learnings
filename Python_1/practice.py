# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 09:12:40 2016

@author: fractaluser
"""

#strings exercises
#write a python program to calculate the length of th estring
str1="The length of the string"
print len(str1)

#Write a Python program to count the number of characters (character frequency) in a string.
def count_char(str1):
    dict={}
    keys=dict.keys()
    for n in str1:
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1
    return dict

print(count_char("google.com"))

#Write a Python program to get a string made of the first 2 and the last 2 chars from a given 
#a string. If the string length is less than 2, return instead the empty string.
def make_string(str1):
    return str1[:2]+str1[-2:]
make_string("Java")

#Write a Python program to get a string from a given string where 
#all occurrences of its first char have been changed to '$', except the first char itself.
text=raw_input()
text1=text.replace(text[0],"$")
text2 = text1[1:]
text3 = text[0] + text2
text3

#Write a Python program to get a single string from two given 
#strings, separated by a space and swap the first two characters of each string
def str_space(a,b):
    return 
x=["a","b","c"]
x=x+["d"]

#reverse the 2 string given
def chars_mix_up(a, b):  
    new_a = b[:2] + a[2:]  
    new_b = a[:2] + b[2:]  
    return new_a + ' ' + new_b  
print(chars_mix_up('abc', 'xyz'))  
a="abcing"
b="xyz"
newa=b[:2]+a[2:]
newb=a[:2]+b[2:]
newa+newb

#add 'ing' to the string having length  greater than 3
def add_ing(s1):
    if len(s1)>2:
        if s1[-3:]=="ing":
            s1+="ly"
        else:
            s1+="ing"
    return s1 
print(add_ing("string")) 

#          