# -*- coding: utf-8 -*-

""" Program you solution to this assignment below using 
    the variable names as defined below.                
    
    Recall that the data for this assignment is contained 
    in a file named length.csv                            """

"""Imports the subpackage matplotlib.pyplot"""
import matplotlib.pyplot as plt 

"""Opens the length csv and reads the data into variable data"""
f_in = open('length.csv', 'r')
data = f_in.readlines()
f_in.close()

"""Cleans the data by dropping whitespace"""
for i in range(len(data)):
    data[i] = data[i].strip()

tweets = list(set(data))                        #gets a list of non-duplicated # of char tweets
charDict = {chars: 0 for chars in tweets}       #creates a dictionary with tweets being the keys
for tweet in data:                              #counts frequency of each # of character tweets
    charDict[tweet] += 1
charList = list(charDict.items())               #assigns dict items to a list
charList = [list(chars) for chars in charList]  #changes the tuples to lists in the list
for i in range(len(charList)):                  #changes the value of first element to a int
    charList[i][0] = int(charList[i][0])
charList.sort(key = lambda x:x[0])              #sorts the list by the # of characters

x = [chars for [chars, freq] in charList]       #assigns the number of characters element to a list
y = [freq for [chars, freq] in charList]        #assigns the frequency element to a list

plt.bar(x, y, align = 'center', color = 'k')    #creates a histogram chart with x and y as the axes
plt.suptitle("Analysis of President Trump's Tweet Length")  #creates a title
plt.xlabel('Number of Characters')                          #creates an x axis label
plt.ylabel('Frequency')                                     #creates a y axis label
plt.xticks(range(0,len(x), 15), [x[i] for i in range(len(x)) if i % 15 == 0])   #changes the ticks based of the x list
plt.gcf().set_size_inches(10, 6)                #changes the size of the graph

plt.savefig('M5Hist.jpg', bbox_inches = 'tight')    #saves the graph into a file called M5Hist.jpg
plt.show()                                          #shows the graph

