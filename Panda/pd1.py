#Panda - Pannel Data
#Series and DataFrame
#Kinda like powerful Excel.

import pandas as pd

ser1 = pd.Series([1,2,3], index = ["A","B","C"])

ser1.iloc[2] = 99

print(ser1.loc["A"])
print(ser1)