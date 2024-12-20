import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ensure the 'outputs' directory exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Load the data
data = pd.read_csv("output/full_dataset_test.csv.gz")

# Melt the ADHD events data
adhd_events = data.melt(
    id_vars=['patient_id', 'sex','dob'],
    value_vars=[f'num_adhd_events_{year}' for year in range(2016, 2024)],
    var_name='year',
    value_name='num_adhd_events'
)

#Computing ADHD disgnosis 

#First this is the total
adhd_total_sex_table = data.groupby(['sex']).count()
adhd_total_sex_table = adhd_total_sex_table.drop(['patient_id','dob'],axis=1)

#Second the the number of adhd dia
#Need to binaries the dia
adhd_dia_sex_table = data.copy()
col_years = [f'num_adhd_events_{year}' for year in range(2016, 2024)]
adhd_dia_sex_table[col_years] = adhd_dia_sex_table[col_years] > 0
adhd_dia_sex_table = adhd_dia_sex_table.groupby(['sex']).sum()
adhd_dia_sex_table = adhd_dia_sex_table.drop(['patient_id','dob'],axis=1)

#Caulcate the prelavence
prevelnce = adhd_dia_sex_table/adhd_total_sex_table

#Need to save the table
prevelnce.to_csv('output/results_saved.csv')