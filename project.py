# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import random as rand
from sys import exit

print("\n-------Welcome to the IE400 Project-------\n")

# global variables
N = 5  # TODO max student amount
N2 = (int) (round(N * np.log(N)))
global_time_matrix = np.zeros((N+1,N+1))
visited_students_list = [0]
travel_time_matrice = []  # holds the travel times matrix
controller = 0

def travelTimeMatrixGenerator(numStudents):

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

def deliverHomeworks(travel_matrix, homework_time_list):
    # This function computes the first minimum non-zero value in the target row
    # then the row number of the min value is set to the column no of the next location
    # the values in visited locations and their symmetry indexes are set to zero 
    # in order not to pass from these locations again 
    global controller # controller points to global 'counter' variable 
    value = 0
    travel_time_value = 0
    for i in range(len(travel_matrix)):
        # the code line below gets the nonzero min element of row number == controller 
        # and passes it to 'value' variable
         
        value = np.min(travel_matrix[controller][np.nonzero(travel_matrix[controller])])
        travel_time_value += value
        #problem is here see the console prints run multiple times
        target = (np.where(travel_matrix == value)[0].tolist()) # target converted to list format 
        print("\nnkdsjfhksjdhflkjshkjh\n", np.where(travel_matrix == value),"\nTarget: ", target)
        x_coordinate = target[0] # target holds the related x and y coordinates[x,y]
        y_coordinate = target[1] # x and y coordinates in target list is passes through x & y variables
        # travel time path for students are printed on console
        #print("Step", i, ": Visited [x,y]: [", x_coordinate," , ", y_coordinate,"] , ", "Value: ", value,"\n")
        travel_matrix[x_coordinate][y_coordinate] = 0
        travel_matrix[y_coordinate][x_coordinate] = 0
        controller = y_coordinate # set controller to y_coordinate
        visited_students_list.append(controller)
        
    print("\nUpdated matrix: \n\n", travel_matrix ,"\n")
    return travel_time_value
    
# create & print sample matrices   
# generate the average matrix from the samples
for i in range(N2):
    print("Matrix ", i+1,":")
    travel_time_matrice = travelTimeMatrixGenerator(N)
    averageMatrixGeneratorV1(travel_time_matrice)
    
averageMatrixGeneratorV2(global_time_matrix,N2)  
homework_times = studyTimeListGenerator(N)
print("\n Average time travel matrix is: ", "\n\n", global_time_matrix)
print("\n\nHomework time matrix is: ", homework_times) 
print("\n\n\n")
print("Total visit time is: ", deliverHomeworks(global_time_matrix,homework_times), "minutes")
print("Visited students:" , visited_students_list)

exit(0)
