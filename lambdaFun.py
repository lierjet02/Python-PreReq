#The below are the lambda function definitions

x = lambda test: 1 if test == True else 0   #returns 1 if True and 0 if False

y = lambda list1: type(list1[0])    #returns type of index 0 of a list

z = lambda num: num * z(num - 1) if num > 1 else 1 #returns the factorial of argument

#Testing x lambda function
print(x(True))
print(x(False))

#Testing y lambda function
print(y(['1', '1', '1']))
print(y([True, 'y', 2]))
print(y([7, False, 10]))
print(y([[1, 2], [2, 3]]))

#Testing z lambda function
print(z(1))
print(z(2))
print(z(5))
