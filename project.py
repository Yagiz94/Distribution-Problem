# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import random as rand
from sys import exit

print("\n-------Welcome to the IE400 Project-------\n")

def travelTimeMatrixGenerator(numStudents):

    #print("Travel Time Matrix:\n")

    # constants
    size = numStudents+1  # we need to include professor so we increase row and column sizes by 1
    bottom = 100
    top = 300

    # 6x6 empty matrix
    arr = np.zeros((size, size))

    # print labels on top of matrix
    #print("Travel Time\t  ", end='')
    #for i in range(size):
        #if i > 0:
            #print("Student", i, " ", end='')

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
            print( (arr[i]))
        else:
            print( (arr[i]))
            

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
maximumStudentAmount = 5  # TODO upper boundary for student amount
N = 10  # TODO current student amount
N2 = (int) (round(N * np.log(N)))

travel_time_matrice = []  # holds the travel times matrix

# initialize lists
for i in range(N2):
    print()
    print("Matrix ", i+1,":")
    print()
    travel_time_matrice = travelTimeMatrixGenerator(N)
    
exit(0)
travel_times = travelTimeMatrixGenerator(N)
homework_times = studyTimeListGenerator(N)
