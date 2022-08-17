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

class PatientsInfo:
    # init methot that takes in each list parameter
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, patients_smoker_statuses,
                 patients_regions, patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges
    
    # method to calculate the average ages of the patients
    
    def analyze_ages(self):
        return ("Average Patient Age: " + str(round(np.average(self.patients_ages))))
    
    #method that calculates the number of males and females
    
    def analyze_sexes(self):
        return    
       
patient_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)
print(patient_info.analyze_ages())