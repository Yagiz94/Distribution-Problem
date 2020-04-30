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

sampleNum = 5

N = sampleNum*np.log(sampleNum)

print("sampleNum: ", sampleNum)

print("N = sampleNum * log(sampleNum): ", int(round(N)))

#TODO for i in range(size):
for i in range(int(round(N))):
    newStudent = rand.sample(range(bottom, top), 1)[0]
    list.append(newStudent)

studentList = np.array(list)
studentList = studentList[1:studentList.size]
print("Student Arr: ", studentList)