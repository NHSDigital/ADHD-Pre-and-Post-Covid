import os
import pandas as pd
import numpy as np
import datetime
from dateutil.relativedelta import relativedelta

from table_wrangle_functions import (
    add_datestamp
)

# Ensure the 'outputs' directory exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Load the data
adhd_medication_data = pd.read_csv("output/Patient_table_3_rolling_6month_incident.csv.gz")

# getting the month and year only
adhd_medication_data['last_mph_med_date'] = (
    pd.to_datetime(adhd_medication_data['last_mph_med_date'], format='%Y-%m-%d')
)

adhd_medication_data['last_mph_med_date_month_date'] = (
    adhd_medication_data['last_mph_med_date'].apply(lambda x: x.strftime('%Y-%m'))
)

output = (
    adhd_medication_data
            .groupby(['last_mph_med_date_month_date','age_band','sex'],as_index=False).size()
)

# Sort values for correct rolling calculation
output = output.sort_values(['age_band', 'sex', 'last_mph_med_date_month_date'])

# Calculate rolling 6-month sum within each group
output['rolling_6_month_sum'] = (
    output
    .groupby(['age_band', 'sex'])['size']
    .rolling(window=6, min_periods=1)
    .sum()
    .reset_index(level=[0,1], drop=True)
)

# Convert 'last_mph_med_date_month_date' to datetime with day as 1st
output['last_mph_med_date_month_date'] = pd.to_datetime(
    output['last_mph_med_date_month_date'] + '-01', format='%Y-%m-%d'
)

# Filter thethe data to only include dates from 2016-04-01 onwards
output = output[output['last_mph_med_date_month_date'] >= '2016-04-01']

# Convert 'last_mph_med_date_month_date' back to string format for final output
output['last_mph_med_date_month_date'] = output['last_mph_med_date_month_date'].dt.strftime('%Y-%m')

#Need to drop the 'size' column as it is not needed anymore
output = output.drop(columns=['size'])

# Adding a small number suppression
rounding_unit = 10
output['rolling_6_month_sum'] = np.ceil(output['rolling_6_month_sum'] / rounding_unit)
output['rolling_6_month_sum'] = output['rolling_6_month_sum'] * rounding_unit

# Adding a set time stamp
output['timestamp'] = add_datestamp()

# Saving the table
output.to_csv("output/Table_3_rolling_6_month_medication.csv")

