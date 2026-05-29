#Searching in a numpy array

import numpy as np

salary = [12000,25000,28000,17000,10000]

np1 = np.array(salary)
x = np1[np.where(np1>15000)]
print(x)


numbers = [24,64,312,689,534,241,567]
np2 = np.array(numbers)

print(np2[np.where(np2%2==0)])
