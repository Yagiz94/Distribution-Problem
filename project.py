# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import random as rand

print("\n-------Welcome to the IE400 Project-------\n")

def travelTimeMatrixGenerator(numStudents):

    print("Travel Time Matrix:\n")

    # constants
    size = numStudents+1  # we need to include professor so we increase row and column sizes by 1
    bottom = 100
    top = 300

    # 6x6 empty matrix
    arr = np.zeros((size, size))

    # print labels on top of matrix
    print("Travel Time\t  ", end='')
    for i in range(size):
        if i > 0:
            print("Student", i, " ", end='')

    # push new line since "end=''" replace '\n' new line character to print labels in the same line
    print()

    # fill the skew symmetric matrix with random variables with values 100 to 300
    for i in range(size):
        for j in range(size):
            # keep main diagonal zero, the rest is symmetric
            if i != j and arr[i, j] == 0:
                arr[i, j] = rand.randint(bottom, top)
                arr[j, i] = arr[i, j]
        if i == 0 :
            print("Professor:\t", (arr[i]))
        else:
            print("Student", i, ":\t", (arr[i]))

    # new line
    print()

    return arr


def studyTimeListGenerator(numStudents):

    # constants1
    bottom = 300
    top = 500

    # generate unique study times for students
    arr = rand.sample(range(bottom, top), numStudents)
    print("Student Study Times: ", arr)

    return arr


#TODO cuurentStudentAmount = 75 # N = 5, 10, 15 ... 75

# TODO we have two possible procedures to find "average matrix"

# TODO 1) we can produce matrices and get average for O(n^3)
#     for i
#       for j
#           produce a matrix
#     for i
#        for j
#            produce N*lnN matrix variations ( N * numpy.log(N) ) -> for k in range(NlnN): travelTimeMatrixGenerator(N)
#            append matrices into an "array of matrices"
#     get average values of from "arra
#     put them into an "average matrix"

def averageMatrixGeneratorV1(numStudents):
    averageArr = []

    # TODO fill here with implementation of average matrix generator

    return averageArr


#TODO 2) we can produce matrices and get average for O(n^3)
# we can produce random variables an put them in a single matrix with O(n^3) as
#    for i
#       for j
#           for k < N*lnN
#               make random values
#               put them into a matrix (average matrix)

def averageMatrixGeneratorV2(numStudents):
    averageArr = []

    # TODO fill here with implementation of average matrix generator

    return averageArr

# TODO (OPTIONAL) maybe it can be reduced to O( N^2 ) or O( N^2 * logN ) but we need to brainstorm over it !!!

#TODO we also need to test everything with different currntStudentAmount(N) so
# we will increment N by 5 in for loop after producing "average matrix" for each N case as
#    for i = 5 to 75
#        N = i
#        averageMatrixGenerator(N)
#        N = N + 5

# general variables
maximumStudentAmount = 75  # TODO upper boundary for student amount

N = 5  # TODO current student amount

# initialize lists
travel_times = travelTimeMatrixGenerator(N)
homework_times = studyTimeListGenerator(N)

exit(0)

# TODO -> exit(0) ignores codes after this line(terminates the program), I am keeping codes below just in case
##################################################################
##################################################################

# variables
studentAmount = 75
bottom = 100
top= 300
total_student_no = 75
coordinate_limit = 150

# arrays
list = [0]
homework_times = []
student_x_coordinates = []
student_y_coordinates = []

# information
N = total_student_no * np.log(total_student_no)
print("total student number: ", total_student_no)
print("N = total student no * log(total student no): ", int(round(N)))

# for i in range(size):
for i in range(int(round(N))): # loop size is N * lnN
    newStudent = rand.sample(range(bottom, top), 1)[0] #create 1 unique random number inside the loop
    list.append(newStudent)

# travel times
travel_times = np.array(list)
travel_times = travel_times[1:travel_times.size]
print("Travel Times Array: ", travel_times)

print(" *************** \t ******************")
print(" *************** \t ******************")
print(" *************** \t ******************")

# homework times
for i in range(studentAmount):
    homework_times.append(rand.randint(300,500))
    
print("Homework Times Array: " , homework_times, "\nlength", len(homework_times))

print(" *************** \t ******************")
print(" *************** \t ******************")
print(" *************** \t ******************")

# x coordinates
for i in range(total_student_no):
    student_x_coordinates.append(rand.randint(0, 150))
    
print("x coordinates to visit", student_x_coordinates, "\nlength", len(student_x_coordinates))

print(" *************** \t ******************")
print(" *************** \t ******************")
print(" *************** \t ******************")

# y coordinates
for i in range(total_student_no):
    student_y_coordinates.append(rand.randint(0, 150))
    
print("y coordinates to visit", student_y_coordinates, "\nlength", len(student_y_coordinates))

print(" *************** \t ******************")
print(" *************** \t ******************")
print(" *************** \t ******************")


