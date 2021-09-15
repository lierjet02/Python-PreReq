# -*- coding: utf-8 -*-

""" Recall that the data for this assignment is called ozoneTemp.csv """
""" Write programming code to create the scatterplot here using the
    variable names below as directed in the assignment.              """

"""Loads the matplotlib.pyplot package"""
import matplotlib.pyplot as plt

"""Opens the file and reads in the lines into data variable"""
f_in = open('ozoneTemp.csv', 'r')
data = f_in.readlines()
f_in.close()

"""Cleans the data by dropping whitespace and splitting the strings"""
for i in range(len(data)):
    data[i] = data[i].strip().split(',')

"""Assigns the column headings to a list and deletes that element from
    original list"""
colHeadings = [head.strip() for head in data[0]]
del data[0]

"""Assigns the elements of Data to a temp list and ozone list"""
x = [int(temp) for ozone, temp in data]
y = [int(ozone) for ozone, temp in data]


plt.scatter(x, y, alpha = 0.5, s = 150)                             #Creates a scatter plot w/ temp on x axis and ozone on y axis
plt.suptitle('Ozone Levels vs Temperature in NYC', fontsize = 20)   #Sets the chart title
plt.xlabel('Temperature (degrees F)', fontsize = 16)                #Labels the x axis
plt.ylabel('Ozone Level', fontsize = 16)                            #Labels the y axis

plt.gcf().set_size_inches(12, 8)                    #changes the size of the chart
plt.savefig('M6oz.jpg', bbox_inches = 'tight')      #saves the chart to a jpg
plt.show()                                          #shows the chart