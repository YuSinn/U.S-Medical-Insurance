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
        print("Average Patient Age: " + str(round(np.average(self.patients_ages))))
    
    # method that calculates the number of males and females
    
    def analyze_sexes(self):
        uniques, counts = np.unique(self.patients_sexes, return_counts = True)    
        print(str(uniques[0]) + ':' + str(counts[0]) + '\n' + str(uniques[1]) + ':' + str(counts[1]))
    
    # method to find each unique region patients are from
    
    def unique_regions(self):
        count = 1
        print('The unique regions are: ')
        for region in np.unique(self.patients_regions):
            print(str(count)+ '. ' + region)
            count += 1
    
    # method to find the average charges
    
    def average_charges(self):
        print('Average Yearly Medical Insurance Charges: $' + str(round(np.average(self.patients_charges),2 )))
    
    # method to find the number of smokers
    
    def analyze_smokers(self):
        uniques, counts = np.unique(self.patients_smoker_statuses, return_counts = True)    
        print('The status of patients that smokes or not. \n' + str(uniques[0]) + ': ' + str(counts[0]) + '\n' + str(uniques[1]) + ': ' + str(counts[1]))
    
    # method to find the number of children
    
    def analyze_num_children(self):
        print('The maximum number of children is: ' + str(max(self.patients_num_children)) + '\n' + "And the average is: " + str(round(np.average(self.patients_num_children), None)))
        
    # method to create dictionary with all patients information
    
    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = [int(age) for age in self.patients_ages]
        self.patients_dictionary['sex'] = self.patients_sexes
        self.patients_dictionary["bmi"] = self.patients_bmis
        self.patients_dictionary['children'] = self.patients_num_children
        self.patients_dictionary["smoker"] = self.patients_smoker_statuses
        self.patients_dictionary["regions"] = self.patients_regions
        self.patients_dictionary["charges"] = self.patients_charges
        return self.patients_dictionary
    
    # method to find out the average per region
    def average_charges_regions(self):
        NE_list = self.patients_charges[(self.patients_regions == 'northeast')]
        NW_list = self.patients_charges[(self.patients_regions == 'northwest')]
        SE_list = self.patients_charges[(self.patients_regions == 'southeast')]
        SW_list = self.patients_charges[(self.patients_regions == 'southwest')]
        print('The average anual charges per region are: \n'+ 'Northeast: ' + str(round(np.average(NE_list),2))+ '\n' + 'Northwest: ' + str(round(np.average(NW_list),2)) + '\n' + 'Southeast: ' + str(round(np.average(SE_list),2)) + '\n' + 'Southwest: ' + str(round(np.average(SW_list),2)))
        
    # method to find out if the smokers pay more than the no smokers
    def smokers_non_smokers(self):
        smokers_charges = self.patients_charges[(self.patients_smoker_statuses == 'yes')]
        non_smokers_charges = self.patients_charges[(self.patients_smoker_statuses == 'no')]
        if np.average(smokers_charges) > np.average(non_smokers_charges):
            print('Smokers has higher insurance charges!')
        else:
            print('Non smokers has higher insurance charges!')
    def full_analyze(self):
        self.analyze_ages()
        self.unique_regions()
        self.analyze_sexes()
        self.average_charges()
        self.average_charges_regions()
        self.smokers_non_smokers()
        self.analyze_num_children()       
patient_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)
patient_info.full_analyze()