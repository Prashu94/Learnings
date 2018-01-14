# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 17:14:39 2017

@author: Prashant Bhat
"""

"""

Problem Defintion: Prediction to survival of passengers on titanic

Dependent variable: Survived
"""

import csv

#Loading and checking data
PATH = "G:\\extra things\\Knowledge\\Python_Practice\\"

train = pd.read_csv(PATH+'train.csv')
test = pd.read_csv(PATH+'test.csv')