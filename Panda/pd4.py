#Dataframe - rows and columns - best way to create this is via a dictionary

import pandas as pd

Students = {"Name": ["Lia","Alex","Zang"],
            "Age" : [19,21,20],
            "Sex" : ['F','M','M'],
            "Grade" : ['A','B','F']}

pd1 = pd.DataFrame(Students, index = ["Student 1","Student 2", "Student 3"])
print(pd1)


#Trying to add a new column

pd1["Class"] = [12,11,10] #TS easy

print(pd1)

#Trying to add a new row:


new_row = pd.DataFrame([{"Name" : "xing" , "Age": 22, "Sex" : 'F', "Grade": 'C', "Class" : 12}], index = ["Student 4"])
pd1 = pd.concat([pd1,new_row])

print(pd1)
