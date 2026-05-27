#In this code we will be talking about the interation of different
#Dimensions of an array

#For a 1D array pretty simple:

import numpy as np

np1 = np.arange(1,11,1)

for i in np1:
    print(i,end = " ")


#To print a 2D array:

np2 = [[1,2,3,4],[5,6,7,8]]
for i in np2:
    #print(np2) #Shows the elements but still as 2D array not individual items
    for j in i:
        print(j)

#But the problem with that is:

#let's say we have a 10 dimensional array, we gotta run 10 loops
#not quite good.

# SO we use the nditer function of numpy library

threeD = np.array([[[1,2],[3,4]],
                    [[4,5],[5,6]]])
print(threeD.shape)

for items in np.nditer(threeD):
    print(items, end = " ")