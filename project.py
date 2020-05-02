# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import random as rand

# variables
studentAmount = 75
bottom = 100
top= 300
total_student_no = 75
coordinate_limit = 150

list = [0]
homework_times = []
student_x_coordinates = []
student_y_coordinates = []


N = total_student_no * np.log(total_student_no)
print("total student number: ", total_student_no)
print("N = total student no * log(total student no): ", int(round(N)))

#TODO for i in range(size):
for i in range(int(round(N))): # loop size is N * lnN
    newStudent = rand.sample(range(bottom, top), 1)[0] #create 1 unique random number inside the loop
    list.append(newStudent)

travel_times = np.array(list)
travel_times = travel_times[1:travel_times.size]
print("Travel Times Array: ", travel_times)

print(" *************** \t ******************")
print(" *************** \t ******************")
print(" *************** \t ******************")

for i in range(studentAmount):
    homework_times.append(rand.randint(300,500))
    
print("Homework Times Array: " , homework_times, "\nlength", len(homework_times))

print(" *************** \t ******************")
print(" *************** \t ******************")
print(" *************** \t ******************")

for i in range(total_student_no):
    student_x_coordinates.append(rand.randint(0, 150))
    
print("x coordinates to visit", student_x_coordinates, "\nlength", len(student_x_coordinates))

print(" *************** \t ******************")
print(" *************** \t ******************")
print(" *************** \t ******************")

for i in range(total_student_no):
    student_y_coordinates.append(rand.randint(0, 150))
    
print("y coordinates to visit", student_y_coordinates, "\nlength", len(student_y_coordinates))

print(" *************** \t ******************")
print(" *************** \t ******************")
print(" *************** \t ******************")
