# Calculating ADHD prevalence rate from EMIS and Cegedim records using open-source data from NHS England

The following code generates the prevalence rate from [NHS England’s Health and Care of People with Learning Disabilities publication series]( https://digital.nhs.uk/data-and-information/publications/statistical/health-and-care-of-people-with-learning-disabilities) The data comes from EMIS and Cegedim.

## Method

### Getting Data
The raw data is downloaded through the following links:
* [For 2016 to 2017](https://files.digital.nhs.uk/49/70A43E/health_care_ld_ccg_data_1617_2021.zip)
* [For 2017 to 2022](https://files.digital.nhs.uk/BC/016738/health_care_ld_sicbl_data_1718_2122.zip)
* [For 2022 to 2023](https://files.digital.nhs.uk/43/BD15AC/health_care_ld_sicbl_2022-23.csv)
* [For 2023 to 2024](https://files.digital.nhs.uk/FC/187D35/health_care_ld_sicbl_2023-24.csv)

The [CCG and SICBL](https://www.nhsbsa.nhs.uk/sicbls-icbs-and-other-providers/organisation-and-prescriber-changes/sub-icb-locations) corresponds to different geographic arrangement of NHS services. The data were taken at different times thus there may be small differences between counts in CCG and SICL. We will only use CCG data for 2016 to 2017 as the SICBL is not available, maintaining data quality where possible.

### Data Munging
All the downloaded table are concatenated, and meta data are harmonised with the outputs from OpenSAFELY.

### Prevalence Calculations
We calculate ADHD prevalence for each year by computing the numerator and denominator as the number patients with ADHD with the indicator `['LDOB089','LDOB091']` and the total sample with the indicator `['LDOB003A' , 'LDOB003B']`. The prevalence are grouped by age, sex and year.

<!--
## Table 
[place_table_here]: #
 -->