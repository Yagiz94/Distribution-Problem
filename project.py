# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as numpy
import random as random

N = 75 # no of students
travel_times = []  #Ti array
homework_times = [] #Xi array

i = random.sample(range(100,500), (int)(N* numpy.log(N)))
travel_times.append(i)

print(travel_times)
print()

for x in range(N):
    x = random.randint(300,500)
    homework_times.append(x)
    
print(homework_times)
