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

# general variables
maximumStudentAmount = 5  # TODO upper boundary for student amount
N = 5  # TODO current student amount
N2 = (int) (round(N * np.log(N)))
global_time_matrix = np.zeros((N+1,N+1))

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
#     get average values of from "array
#     put them into an "average matrix"

def averageMatrixGeneratorV1(travel_time):

    # TODO fill here with implementation of average matrix generator
    # Take the overall sum of eacch matrix's [i][j] values and pass these overal sums to global_time_matrix
    for i in range(len(travel_time)):
        for j in range(len(travel_time)):
            global_time_matrix[i][j] += travel_time[i][j]


#TODO 2) we can produce matrices and get average for O(n^3)
# take the global_time matrix and divide each value to N2 in order to get average values in the matrix
def averageMatrixGeneratorV2(global_list_time, avgNo):
   for i in range(len(global_list_time)):
        for j in range(len(global_list_time)):
            global_list_time[i][j] = (int) (round(global_list_time[i][j] / avgNo))


# TODO (OPTIONAL) maybe it can be reduced to O( N^2 ) or O( N^2 * logN ) but we need to brainstorm over it !!!

#TODO we also need to test everything with different currntStudentAmount(N) so
# we will increment N by 5 in for loop after producing "average matrix" for each N case as
#    for i = 5 to 75
#        N = i
#        averageMatrixGenerator(N)
#        N = N + 5


travel_time_matrice = []  # holds the travel times matrix

# initialize lists
for i in range(N2):
    print()
    print("Matrix ", i+1,":")
    print()
    travel_time_matrice = travelTimeMatrixGenerator(N)
    averageMatrixGeneratorV1(travel_time_matrice)
    
averageMatrixGeneratorV2(global_time_matrix,N2)  
print("global matrix is: ", "\n\n", global_time_matrix)    
exit(0)
travel_times = travelTimeMatrixGenerator(N)
homework_times = studyTimeListGenerator(N)



