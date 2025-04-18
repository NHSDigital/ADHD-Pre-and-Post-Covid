import os
import pandas as pd
import numpy as np

# Ensure the 'outputs' directory exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Load the data
adhd_data = pd.read_csv("output/adhd_dataset.csv.gz")

week_bin = [0, 1, 2, 4, 8, 12, 21, 52, 104]

# Placing into a histogram
adhd_data['year_of_diagnosis'] = pd.DatetimeIndex(adhd_data['first_adhd_diagnosis_date']).year

# Need to collect the counts
output = adhd_data.groupby(['year_of_diagnosis', pd.cut(adhd_data.times_between_dia_med_weeks, week_bin)])
output = output.size().unstack()

# Small number supppression
rounding_unit = 10
output = np.ceil((output / rounding_unit))
output = output * rounding_unit

# Saving the table
output.to_csv("output/adhd_dia_med_gap_weeks.csv")
