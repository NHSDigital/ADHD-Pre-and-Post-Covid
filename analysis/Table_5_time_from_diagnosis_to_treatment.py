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

# Convert medication date column to datetime if not already
adhd_medication_date_data['first_mph_med_date'] = pd.to_datetime(adhd_medication_date_data['first_mph_med_date'])

# Filter out rows where 'first_mph_med_date' is before 2016-04-01
adhd_medication_date_data = adhd_medication_date_data[adhd_medication_date_data['first_mph_med_date'] >= '2016-04-01']

# Create a 'year_of_medication' column that groups April-March as a year
adhd_medication_date_data['year_of_medication'] = adhd_medication_date_data['first_mph_med_date'].apply(
    lambda x: x.year if x.month >= 4 else x.year - 1
)

#Making the year of medication a clearer
adhd_medication_date_data['year_of_medication'] = adhd_medication_date_data['year_of_medication'].astype(str) + '-' + (adhd_medication_date_data['year_of_medication'] + 1).astype(str)

# Generating the final table
output = adhd_medication_date_data.groupby(['age_band', 'year_of_medication', 'sex'], as_index=False).times_between_dia_med_weeks.agg(['mean', 'median', 'size'])

# #Adding a small number suprresion
rounding_unit = 10
output['size'] = np.ceil(output['size'] / rounding_unit)
output['size'] = output['size'] * rounding_unit

# #Adding a set time stamp
output['timestamp'] = add_datestamp()

# Saving the table
output.to_csv("output/Table_5_time_from_diagnosis_to_treatment.csv")

