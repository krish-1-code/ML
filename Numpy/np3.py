#Copy vs View

import numpy as np

np1 = np.array([1,2,3,4,5])

np2 = np1.view()
np3 = np1.copy()

print(f"NP2 = {np2}")
print(f"NP3 = {np3}")

#Changing the original array

np1[0] = 67

print(f"Np1 = {np1}")
print(f"Np2 = {np2}")
print(f"Np3 = {np3}")
