import os
import pandas as pd
import numpy as np

from table_wrangle_functions import (
    add_datestamp
)

#The parameters
start_date_string = "2016-04-01"
start_date = pd.to_datetime(start_date_string, format='%Y-%m-%d')

end_date_point = "2025-04-01"
end_date = pd.to_datetime(end_date_point, format='%Y-%m-%d')


# Ensure the 'outputs' directory exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Load the data
adhd_medication_date_data = pd.read_csv("output/Patient_table_5_dia_to_med.csv.gz")

# Convert medication date column to datetime if not already
adhd_medication_date_data['first_mph_med_date'] = pd.to_datetime(adhd_medication_date_data['first_mph_med_date'], format='%Y-%m-%d')

# Filter out rows with the defined the first and end point
adhd_medication_date_data = adhd_medication_date_data[adhd_medication_date_data['first_mph_med_date'] >= start_date]
adhd_medication_date_data = adhd_medication_date_data[adhd_medication_date_data['first_mph_med_date'] < end_date] # The end date is the start of the next tax year


# Create a 'year_of_medication' column that groups April-March as a year
adhd_medication_date_data['year_of_medication'] = adhd_medication_date_data['first_mph_med_date'].apply(
    lambda x: x.year if x.month >= 4 else x.year - 1
)

#Making the year of medication a clearer
adhd_medication_date_data['year_of_medication'] = adhd_medication_date_data['year_of_medication'].astype(str) + '-' + (adhd_medication_date_data['year_of_medication'] + 1).astype(str)

#Need to check the simpsion paradox

list_of_combination = [
    ['age_band', 'year_of_medication', 'sex'],
    ['age_band', 'year_of_medication'],
    ['year_of_medication', 'sex'],
    ['year_of_medication'],
    ]

output_to_save = pd.DataFrame()

for each_cobination in list_of_combination:
    # Generating the final table
    output = adhd_medication_date_data.groupby(each_cobination, as_index=False).times_between_dia_med_weeks.agg(['mean', 'median', 'size'])

    # #Adding a small number suprresion
    rounding_unit = 10
    output['size'] = np.ceil(output['size'] / rounding_unit)
    output['size'] = output['size'] * rounding_unit

    #Rounding the weeks
    output[['mean', 'median']] = output[['mean', 'median']].round(0).astype(int)

    output_to_save = pd.concat([output_to_save,output], axis=0, ignore_index=True)
    output_to_save = output_to_save.fillna('ALL')

# #Adding a set time stamp
output_to_save['timestamp'] = add_datestamp()

# Saving the table
output_to_save.to_csv("output/Table_5_time_from_diagnosis_to_treatment.csv")

