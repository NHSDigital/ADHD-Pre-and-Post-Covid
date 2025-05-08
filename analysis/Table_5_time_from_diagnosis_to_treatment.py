import os
import pandas as pd
import numpy as np

from table_wrangle_functions import (
    add_datestamp
)

# Ensure the 'outputs' directory exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Load the data
adhd_medication_date_data = pd.read_csv("output/Patient_table_5_dia_to_med.csv.gz")

#Genrating the final table
output = adhd_medication_date_data.groupby('year_of_medication').times_between_dia_med_weeks.agg(['mean', 'median'])

#Adding a set time stamp
output['timestamp'] = add_datestamp()

# Saving the table
output.to_csv("output/Table_5_time_from_diagnosis_to_treatment.csv")

