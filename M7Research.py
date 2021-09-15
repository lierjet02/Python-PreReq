# -*- coding: utf-8 -*-

import numpy as np

""" Complete your solution to the first research task here, which 
    involves the data file named temperatures.csv and using the 
    variable names as directed in the assignment.                 """

"""Open file and read in data"""    
f_in = open('temperatures.csv', 'r', encoding = 'ISO-8859-1')
data = f_in.readlines()
f_in.close()

"""Cleans the data by stripping and slicing off '°F' """
for i in range(len(data)):
    data[i] = data[i].strip()
    if data[i].endswith(' °F'):
        data[i] = data[i][:-3]

myTemps = [float(i) for i in data]  #list comprehension to create float list out of data
print(myTemps)

""" Complete your soution to the second research task here, which 
    involves combining numpy arrays                               """
x = np.array([0,1,2,3])
y = np.array([4,5,6,7])
z = np.stack((x, y), axis = 1)  #uses stack function to join the arrays along axis 1
print(z)