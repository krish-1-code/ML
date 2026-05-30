import pandas as pd

# 1. Setup the initial dictionary (3 items per key)
Students = {
    "Name": ["Lia", "Alex", "Zang"],
    "Age": [19, 21, 20],
    "Sex": ['F', 'M', 'M'],
    "Grade": ['A', 'B', 'F']
}

# 2. Create DataFrame (Matching with exactly 3 index labels)
pd1 = pd.DataFrame(Students, index=["Student 1", "Student 2", "Student 3"])
print("--- Initial DataFrame ---")
print(pd1)
print("\n")

# 3. Add a new column (3 elements for 3 rows)
pd1["Class"] = [12, 11, 10]
print("--- After Adding Class Column ---")
print(pd1)
print("\n")

# 4. Create the new row DataFrame with a matching index label
new_row = pd.DataFrame(
    [{"Name": "xing", "Age": 22, "Sex": 'F', "Grade": 'C', "Class": 12}],
    index=["Student 4"]
)

# 5. Concatenate passing them inside a list []
pd1 = pd.concat([pd1, new_row])

print("--- After Adding New Row ---")
print(pd1)