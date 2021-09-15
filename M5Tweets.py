# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 16:08:38 2018

@author: jrbrad
"""

""" The list below contains words that you are to exclude form your analysis """
stopWords = ['to', 'the', 'a', 'to', 'is', 'and', 'in', 'of', 'that', 'it', 'be','at', 'this', 'are', 'be', 'for', 'will', 'with', 'at', 'have','on','&amp', 'by']

""" Program you solution to this assignment below using 
    the variable names as defined below.                """

"""Imports the subpackage matplotlib.pyplot"""    
import matplotlib.pyplot as plt

"""Opens the length csv and reads the data into variable data"""
f_in = open('words.csv', 'r', encoding = 'ISO-8859-1')
data = f_in.readlines()
f_in.close()

"""Cleans the data by dropping whitespace and only including words not in stopWords"""
for i in range(len(data)):
    data[i] = data[i].strip()    
data = [word for word in data if word not in stopWords]
    
words = list(set(data))                             #gets a list of non-duplicated words
wordDict = {word: 0 for word in words}              #creates a dictionary with words as the key
for word in data:                                   #counts frequency of the words in data
    wordDict[word] += 1
wordList = list(wordDict.items())                   #creates a list of words and frequencies out of the dictionary items
wordList = [list(words) for words in wordList]      #changes the type to list from tuple
wordList.sort(key = lambda x:x[1], reverse = True)  #sorts list on the most used words
numPlot = 10
wordList = wordList[:numPlot]                       #slices the list to only include 10 most used words
    
x = [word for [word, freq] in wordList]             #assigns the top 10 words to a list
y = [freq for [word, freq] in wordList]             #assigns the frequencies of those words to a list

"""Creates a fig and ax variable"""
fig,ax = plt.subplots()                             

"""Modifies the ax properties and methods"""
ax.bar(x, y, align = 'center', color = 'k')                        #creates a histogram with x and y as the axes
ax.xaxis.set_label_text("Words in Trump's Tweets", fontsize = 14)  #creates an x axis label
ax.yaxis.set_label_text('Number of Occurrences', fontsize = 14)    #creates a y axis label

"""Modifies the fig properties and methods"""
fig.suptitle("President Trump's Most Tweeted Words", fontsize = 20)  #creates a title
fig.set_size_inches(12, 6)                                           #changes the size of the graph 

plt.savefig('tweets.jpg', bbox_inches = 'tight')    #saves the graph as a jpg
plt.show()                                          #shows the graph