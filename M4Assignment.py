# -*- coding: utf-8 -*-

def select(students, index):   #accepts two arguments, a dictionary or its keys and an index
    if type(students) == 'dict':        #lines 4-7 convert keys into list depending on argument type
       keys = list(students.keys())
    else:
        keys = list(students)
    keySelect = []              #sets an empty list
    for i in keys:              #fills list with elements from the specified index
        keySelect.append(i[index])
    dedup = list(set(keySelect)) #creates a list of non-duplicated elements
    dedup.sort()                #sorts the list
    return dedup
    
studentPerf = {('Jeffery','male','junior'):[0.81,0.75,0.74,0.8],
('Able','male','senior'):[0.87,0.79,0.81,0.81],
('Don','male','junior'):[0.82,0.77,0.8,0.8],
('Will','male','senior'):[0.86,0.78,0.77,0.78],
('John','male','junior'):[0.74,0.81,0.87,0.73],
('Patrick','male','senior'):[0.9,0.82,0.94,0.79],
('Iggie','male','senior'):[0.8,0.88,0.87,0.88],
('Harvey','male','sophomore'):[0.66,0.76,0.79,0.76],
('Ralph','male','senior'):[0.81,0.78,0.8,0.89],
('Edward','male','senior'):[0.81,0.87,0.88,0.84],
('Eric','male','junior'):[0.76,0.73,0.83,0.76],
('Wallace','male','sophomore'):[0.7,0.8,0.79,0.8],
('Ronald','male','senior'):[0.76,0.78,0.82,0.83],
('Perry','male','junior'):[0.83,0.87,0.77,0.75],
('Robert','male','senior'):[0.92,0.8,0.82,0.84],
('Thomas','male','junior'):[0.76,0.72,0.8,0.72],
('Mark','male','senior'):[0.87,0.79,0.81,0.83],
('Santiago','male','junior'):[0.77,0.81,0.74,0.75],
('Diego','male','senior'):[0.78,0.8,0.8,0.8],
('Samuel','male','senior'):[0.8,0.89,0.82,0.87],
('Alejandro','male','senior'):[0.86,0.79,0.87,0.8],
('Hector','male','junior'):[0.79,0.72,0.78,0.72],
('Jin','male','senior'):[0.83,0.79,0.9,0.8],
('Yu Yan','male','junior'):[0.75,0.72,0.8,0.81],
('Fei Hung','male','senior'):[0.86,0.91,0.84,0.9],
('Chen','male','senior'):[0.76,0.77,0.84,0.88],
('Wei','male','senior'):[0.84,0.86,0.78,0.88],
('Fang','male','senior'):[0.78,0.89,0.89,0.86],
('Anders','male','junior'):[0.8,0.73,0.78,0.8],
('Nils','male','junior'):[0.82,0.84,0.79,0.76],
('Arne','male','sophomore'):[0.68,0.73,0.81,0.72],
('Jochen','male','junior'):[0.82,0.86,0.8,0.73],
('Jurgen','male','junior'):[0.68,0.78,0.78,0.81],
('Carl','male','junior'):[0.72,0.82,0.79,0.76],
('Thor','male','senior'):[0.91,0.84,0.9,0.89],
('Harold','male','junior'):[0.76,0.78,0.8,0.79],
('Aditya','male','senior'):[0.83,0.87,0.82,0.83],
('Varun','male','senior'):[0.76,0.86,0.88,0.79],
('Shantanu','male','senior'):[0.79,0.81,0.78,0.78],
('Krishnan','male','sophomore'):[0.66,0.76,0.74,0.8],
('Manoj','male','junior'):[0.75,0.77,0.72,0.81],
('Rahul','male','sophomore'):[0.73,0.67,0.68,0.7],
('Rohit','male','sophomore'):[0.75,0.75,0.77,0.74],
('Vijay','male','senior'):[0.91,0.84,0.83,0.9],
('Sophie','female','senior'):[0.83,0.96,0.9,0.95],
('Lynn','female','senior'):[0.97,0.85,0.93,0.88],
('Bailey','female','sophomore'):[0.83,0.78,0.74,0.75],
('Karen','female','junior'):[0.79,0.88,0.9,0.84],
('Audrey','female','junior'):[0.79,0.85,0.86,0.81],
('Suzie','female','junior'):[0.81,0.82,0.93,0.88],
('Marissa','female','senior'):[1,0.92,0.95,0.91],
('Hong','female','senior'):[0.92,0.93,0.88,1],
('Susudio','female','sophomore'):[0.75,0.85,0.85,0.81],
('Clarissa','female','junior'):[0.79,0.84,0.82,0.83],
('Layla','female','junior'):[0.87,0.88,0.87,0.92],
('Alanis','female','sophomore'):[0.75,0.77,0.76,0.81],
('Erin','female','senior'):[0.88,0.93,0.97,0.91],
('Chantel','female','junior'):[0.85,0.84,0.85,0.79],
('Laura','female','junior'):[0.82,0.84,0.94,0.88],
('Laurie','female','senior'):[0.86,0.93,0.89,0.94],
('Elle','female','senior'):[0.98,0.92,0.98,0.99],
('Alisa','female','sophomore'):[0.75,0.86,0.89,0.83],
('Else','female','junior'):[0.91,0.8,0.84,0.88],
('Anna','female','senior'):[0.88,0.95,0.97,0.83],
('Dorothy','female','junior'):[0.94,0.94,0.89,0.84],
('Bridgette','female','junior'):[0.85,0.8,0.84,0.8],
('Sophia','female','senior'):[0.93,0.96,0.94,0.87],
('Bianca','female','junior'):[0.83,0.79,0.93,0.9],
('Mia','female','junior'):[0.89,0.85,0.89,0.91],
('Monika','female','junior'):[0.89,0.82,0.9,0.91],
('Emma','female','senior'):[0.96,0.85,0.88,0.97],
('Margaurite','female','junior'):[0.88,0.86,0.85,0.79],
('Helga','female','senior'):[0.9,0.85,0.84,0.89],
('Patsy','female','junior'):[0.84,0.88,0.9,0.86],
('Phoebe','female','senior'):[0.85,0.94,0.88,0.97],
('Vivian','female','junior'):[0.78,0.86,0.89,0.77],
('Breeanne','female','sophomore'):[0.74,0.82,0.84,0.85],
('Charlotte','female','junior'):[0.77,0.84,0.87,0.77],
('Amelia','female','senior'):[0.87,1,0.89,0.92],
('Olivia','female','junior'):[0.84,0.78,0.85,0.91],
('Isabella','female','sophomore'):[0.78,0.86,0.83,0.8],
('Evelyn','female','junior'):[0.85,0.88,0.91,0.88],
('Abagail','female','senior'):[0.93,0.94,0.87,0.84],
('Ella','female','sophomore'):[0.75,0.82,0.76,0.87],
('Ava','female','junior'):[0.88,0.83,0.9,0.81],
('Madison','female','senior'):[0.93,0.97,0.9,0.95],
('Chloe','female','junior'):[0.88,0.88,0.94,0.84],
('Grace','female','junior'):[0.9,0.85,0.88,0.83],
('Aubrey','female','junior'):[0.83,0.77,0.83,0.8],
('Mila','female','sophomore'):[0.82,0.85,0.79,0.83],
('Zoe','female','sophomore'):[0.82,0.81,0.83,0.81],
('Leah','female','sophomore'):[0.8,0.84,0.78,0.75],
('Stella','female','senior'):[0.93,0.9,0.96,0.92],
('Claire','female','sophomore'):[0.83,0.79,0.86,0.86],
('Aurora','female','senior'):[0.92,0.87,0.91,0.9],
('Lucy','female','senior'):[0.82,0.82,0.96,0.88],
('Samantha','female','senior'):[0.92,0.95,1,0.93],
('Tabitha','female','senior'):[0.97,0.87,0.89,0.88]}

# Complete the main program code below using the listed variables 

sophNames = [names[0] for names in studentPerf.keys() if names[2] == 'sophomore']   #creates a list of names of sophomores
print(sophNames)

classes = select(studentPerf, 2)    #creates a list of unique classes
print(classes)

genders = select(studentPerf.keys(), 1) #creates a list of unique genders
print(genders)

dictAvgGrade = {key:(sum(studentPerf[key]) / len(studentPerf[key])) for key in studentPerf} #creates a dictionary of each student average grade
print(dictAvgGrade)

gradesSoph = [value for key, value in dictAvgGrade.items() if key[2] == 'sophomore']    #creates a list of the average grade of sophomores
print(gradesSoph)

dictDemClass = {year: 0 for year in classes}    
print(dictDemClass)

jun = 0
sen = 0
soph = 0
for i in studentPerf.keys():    #for loop to count the occurrances of each grade
    if i[2] == 'sophomore':
        soph += 1
    elif i[2] == 'junior':
        jun += 1
    else:
        sen += 1
dictDemClass.update({'sophomore': soph, 'junior': jun, 'senior': sen})  #updates the dictionary with the number of students per grade
print(dictDemClass)

dictDemGender = {gender:0 for gender in genders}
print(dictDemGender)

male = 0
female = 0
for i in studentPerf.keys():    #for loop to count the occurances of each gender
    if i[1] == 'male':
        male += 1
    else:
        female += 1
dictDemGender.update({'female': female, 'male': male})  #updates the dictionary with the number of students per gender
print(dictDemGender)

dictGradeClass = {year: 0 for year in classes}  #creates empty dictionary like dictDemClass
jun = 0
sen = 0
soph = 0
junGrades = 0
senGrades = 0
sophGrades = 0
for i in dictAvgGrade.items():  #for loop that adds the values of dictionary and counts per grade
    if i[0][2] == 'sophomore':
        soph += 1
        sophGrades += i[1]
    elif i[0][2] == 'junior':
        jun += 1
        junGrades += i[1]
    else:
        sen += 1
        senGrades += i[1]
dictGradeClass.update({'sophomore': sophGrades / soph, 'junior': junGrades / jun, 'senior': senGrades / sen})
print(dictGradeClass)