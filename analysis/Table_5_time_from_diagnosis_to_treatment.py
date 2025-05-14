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
output = adhd_medication_date_data.groupby(['year_of_medication','sex']).times_between_dia_med_weeks.agg(['mean', 'median','size'])

# #Filter the muilple index
output = output[output.index.isin(list(range(2016,2025)), level=0)]

# #Adding a small number suprresion
rounding_unit = 10
output['size'] = np.ceil(output['size'] / rounding_unit)
output['size'] = output['size'] * rounding_unit

# #Adding a set time stamp
output['timestamp'] = add_datestamp()

# Saving the table
output.to_csv("output/Table_5_time_from_diagnosis_to_treatment.csv")

