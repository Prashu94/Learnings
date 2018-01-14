# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 09:18:26 2016

@author: fractaluser
"""

#Assignment 01
import re
from collections import Counter
import matplotlib.pyplot as plt

f1=open('/home/fractaluser/Desktop/learning/Python/word_freq_ini.txt','r')
txt1=f1.read()
f1.close()
txt1=txt1.lower()
txt2=re.sub('[^a-z]','',txt1)
cnt=Counter(txt2)


plt.bar(range(len(cnt)),cnt.values(),align='center')
plt.xticks(range(len(cnt)),cnt.keys())
plt.show()


f2=open('/home/fractaluser/Desktop/learning/Python/analyse.txt','r')
txt=f2.read()
f2.close()
txt3=txt.lower()
txt4=re.sub('[^a-z]','',txt3)
cnt1=Counter(txt4)

plt.bar(range(len(cnt1)),cnt1.values(),align='center')
plt.xticks(range(len(cnt1)),cnt1.keys())
plt.show()

# In the first graph the most frequent letter is 'e'
# In the second Graph the most frequent letter is 'l'
#Hence it is seen that there is a shift of 7 charaacters in the file 
#If we want to bring the file in its original format by removing the excess 
#l's we do the following step i.e shifting it back by 7

txtout=''
for i in txt4:
    txtout+=chr(ord(i)-7)
txtout=txtout.lower()
txtout1=re.sub('[^a-z]','',txtout)
cnt2=Counter(txtout1)

plt.bar(range(len(cnt2)),cnt2.values(),align='center')
plt.xticks(range(len(cnt2)),cnt2.keys())
plt.show()
