import os
import pandas as pd
import numpy as np
from datetime import (
    datetime
)
from dateutil.relativedelta import relativedelta

from table_wrangle_functions import (
    add_datestamp,
    rolling_6_month_sum
)

# The key parameters
rolling_col_name = 'rolling_6_month_sum'
threshold_start_date = pd.to_datetime('2016-04-01', format='%Y-%m-%d') 
date_column = 'last_mph_med_date_month_date'
count_column = 'size'
column_group = ['sex','age_band']
start_date = threshold_start_date - relativedelta(months=7)
end_date =pd.to_datetime("2025-04-01", format='%Y-%m-%d')

# Ensure the 'outputs' directory exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Load the data
adhd_medication_data = pd.read_csv("output/Patient_table_3_rolling_6month_incident.csv.gz")

# getting the month and year only
adhd_medication_data['last_mph_med_date'] = (
    pd.to_datetime(adhd_medication_data['last_mph_med_date'], format='%Y-%m-%d')
)

#This is a crude way of removing the day
adhd_medication_data[date_column] = (
    adhd_medication_data['last_mph_med_date'].apply(lambda x: x.strftime('%Y-%m'))
)

adhd_medication_data[date_column] = (
    pd.to_datetime(adhd_medication_data[date_column], format='%Y-%m')
)

grouping_cols = [date_column] + column_group
output = (
    adhd_medication_data
            .groupby(grouping_cols, as_index=False).size()
)

output = (
    rolling_6_month_sum(
        output,
        start_date,
        end_date, 
        date_column,
        count_column,
        column_group,
        rolling_col_name)
)

# Filter to the start and end date
output = output[output[date_column] >= threshold_start_date]

# Drop the size count
output = output.drop(columns=[count_column])

# Adding a small number suppression
rounding_unit = 10
output['rolling_6_month_sum'] = np.ceil(output['rolling_6_month_sum'] / rounding_unit)
output['rolling_6_month_sum'] = output['rolling_6_month_sum'] * rounding_unit

# Adding a set time stamp
output['timestamp'] = add_datestamp()

# Saving the table
output.to_csv("output/Table_3_rolling_6_month_medication.csv")

