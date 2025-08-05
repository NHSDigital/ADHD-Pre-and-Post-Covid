import pandas as pd
import requests
from config import config
import os
import zipfile
import utils

# Check if any required CSV file is missing, then download if needed
missing_files = [
    fname for fname in config['list_of_csv'].values()
    if not os.path.isfile(os.path.join(config['file_path_to_save'], fname))
]
if missing_files:
    utils.create_source_files_from_nhs_england(config)

dict_of_files = config['list_of_csv']

combined_table_emis = pd.DataFrame()

for each_key in list(dict_of_files.keys()):

    #opening each file
    each_csv = pd.read_csv(config['file_path_to_save'] + dict_of_files[each_key])
    
    #Wrangle the file to match OS's outputs
    each_ratio = utils.wrangling_table_to_opensafely_form(each_csv,each_key,config)

    combined_table_emis = pd.concat([combined_table_emis,each_ratio], axis=0, ignore_index=True)

combined_table_emis.to_csv(config['file_path_to_emis_measure'])