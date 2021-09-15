# -*- coding: utf-8 -*-

""" Program you solution to this assignment below using 
    the variable names as defined below                 """

f_in = open('states.csv', 'r')  #opens up a file called states.csv
statesData = f_in.readlines()   #reads the lines from the csv into a list
f_in.close()    #closes the file

for i in range(len(statesData)):
    statesData[i] = statesData[i].strip().split(',')    #drops all whitespace and splits the string into a list
    if i != 0:  #this is so the first line of headers is not ran in the type conversion below
        statesData[i] = [str(statesData[i][0]), int(statesData[i][1]), int(statesData[i][2]),   #converts the type of each element in the list of lists
                         float(statesData[i][3]), float(statesData[i][4])]
print(statesData)

sums = list()   #creates an empty list
for y in range(len(statesData[0])): #iterates through the individual states list
    temp = 0    #sets a temporary variable to 0
    if y !=0:   #this ignores the first element of each states list i.e 'State'
        for x in range(len(statesData)):    #iterates through the main part of the list
            if x != 0:  #ignores the headers list at beginning of statesData
                temp += statesData[x][y]    #sums up all elements in statesData that are in a specific 'column' i.e. 'Population'
        sums.append(temp) #adds the total of the 'column' to the sums list
print(sums)