import numpy as np

#Sorting Numpy Array:

#for int values its the ascending order

list1 = [1,8,3,6,2]
np1 = np.array(list1)

print(np.sort(np1))
print(np1)


#For alphabatical order:
#A - Z then a to z

list2 = ['Z','C','x','a','B','T','u','L','w']
np2 = np.array(list2)
print(np.sort(np2))
print(np2)

#For Booleans:
#first false then True cuz false = 0 and True = 1; 0 < 1

list3 = [True,False,False,True,True,True,False,False]
np3 = np.array(list3)
print(np.sort(np3))
print(np3)

#Sorting a multi dimensional arary:

list4 = [[1,6,2,5,9,3],
         ['a','Z','x','B','T','y']]

np4 = np.array(list4)
print(np4)
print(np.sort(np4))