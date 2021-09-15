# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:38:57 2018

@author: jrbrad
"""

data = [['Jun',4.3],['Jul',4.3],['Aug',4.4],['Sep',4.2],['Oct',4.1],['Nov',4.1],['Dec',4.1],['Jan',4.1],['Feb',4.1],['Mar',4.1],['Apr',3.9],['May',3.8],]

""" Program you solution to this assignment below using 
    the variable names as defined below                 """
    
# Imports the matplotlib subpackage
import matplotlib.pyplot as plt

# Creates a list of x and y variables off the above data list using list comprehension    
x = [datum[0] for datum in data]   
y = [datum[1] for datum in data]

plt.plot(y)                             #plots the y list
plt.suptitle('U.S. Unemployment Rate')  #creates a title for the plot
plt.xlabel('Month')                     #labels the x axis
plt.ylabel('Unemployment Rate (%)')     #labels the y axis
plt.xticks(range(len(x)), x)            #assigns the list: x to the x axis's tick marks
plt.show()                              #displays the plot
