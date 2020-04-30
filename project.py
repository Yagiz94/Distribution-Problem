# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import random as rand

studentAmount = 75
list = [0]

bottom = 100
top= 300
sampleNum = 75

N = sampleNum*np.log(sampleNum)

print("sampleNum: ", sampleNum)

print("N = sampleNum * log(sampleNum): ", int(round(N)))

#TODO for i in range(size):
for i in range(int(round(N))): # loop size is N * lnN
    newStudent = rand.sample(range(bottom, top), 1)[0] #create 1 unique random number inside the loop
    list.append(newStudent)

travel_times = np.array(list)
travel_times = travel_times[1:travel_times.size]
print("Travel Times Arr: ", travel_times)
