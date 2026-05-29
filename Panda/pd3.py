#Turn a dictionary into a series:

import pandas as pd

earn = {"Sunday" : 0,
        "Monday" : 80,
        "Tuesday": 90,
        "Wednesday": 85,
        "Thursday": 95,
        "Friday": 100,
        "Satuday": 0}

ser = pd.Series(earn)
print(ser)

#Filtering the earnings

morethan80 = ser[ser>80]
print(morethan80)

#Zero_Earning

zero = ser[ser == 0]
print(zero)
