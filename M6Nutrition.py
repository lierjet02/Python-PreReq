# -*- coding: utf-8 -*-

import numpy as np
from numpy import linalg

""" Solve the nutritional programming problem here using the variable x
    for your solution                                                   """

"""A represents the calories, protein and fat in the rows and 
    type of cereal in the column"""    
A = np.array([[105,130,120],[1,3,5],[2,4,2]])   
b = [[245],[6],[7]]        #vector of target calories, protein and fat in the cereal mix                 
x = linalg.solve(A, b)      #Finds the vector x in the equation Ax = b 


print(A.dot(x))     #Prints Ax to show it is equal to b