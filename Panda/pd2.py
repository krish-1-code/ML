#Searching and filtering series

import pandas as pd

salary = [90000,86000,56000,40000,99000,101000,20000]

ser1 = pd.Series(salary)

print(ser1[ser1>=50000])