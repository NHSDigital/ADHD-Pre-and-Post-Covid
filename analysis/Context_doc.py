import os
import pandas as pd
import numpy as np

from table_wrangle_functions import (
    add_datestamp
)

#Need to read in the README.md text file
readme_file_path = 'analysis/README.md'
with open(readme_file_path,"r") as f:
    readme_string = f.read()

time_stamp_string = 'Created on ' + add_datestamp() + '\n'

output_string = time_stamp_string + readme_string


# Ensure the 'outputs' directory exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(output_dir, "context.txt"), "w") as f:
    f.write(output_string)
