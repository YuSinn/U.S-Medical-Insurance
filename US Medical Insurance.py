# Python project : "U.S Medical Insurance"
# Vladut Alexandru Gabriel
# Version 0.1

import pandas as pd
import numpy as np

# creating the insurance.csv dataframe
ins_df = pd.read_csv("insurance.csv")

# listing first 5 rows
#print(ins_df.head())

# creating list with every column from the dataframe
ages = ins_df.age
sexes = ins_df.sex
bmis = ins_df.bmi
num_children = ins_df.children
smoker_statuses = ins_df.smoker
regions = ins_df.region
insurance_charges = ins_df.charges

print(round(np.average(ages),0))
       
    