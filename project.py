# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# libraris
import pandas as pd
import numpy as np
import random as rand

# constants
sampleNum = 5
studentAmount = 75
bottom = 100
top= 300

# initialized list for travel times
list = [0]

# number of generatable path variations
N = sampleNum*np.log(sampleNum)

# description of travel time methodology
print("sampleNum: ", sampleNum)
print("N = sampleNum * log(sampleNum): ", int(round(N)))

# procedure to generate array of path variations
#TODO for i in range(size):
for i in range(int(round(N))):
    newStudent = rand.sample(range(bottom, top), 1)[0]
    list.append(newStudent)

# convert the list of paths to numpy array
studentList = np.array(list)
studentList = studentList[1:studentList.size]
print("Student Arr: ", studentList)