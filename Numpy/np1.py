import numpy as np

np1 = np.array([1,2,3,4,5])
print(np1)

list1 = [6,7,8,9,10]
np2 = np.array(list1)
print(np2)

#arange function

np3 = np.arange(10)
print(np3)

np4 = np.arange(1,5,1)
print(np4)

npx = np.array([[1,2,3],
                [4,5,6],
                [6,7,8]])

print(npx.shape)

npz = np.full((3),9)
print(npz)

npy = np.full((2,5),'*')
print(npy)