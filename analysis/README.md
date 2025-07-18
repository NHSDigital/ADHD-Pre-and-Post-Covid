# List of Outputs

The purpose of this document is to provide context of each file as requested in the [documentation](https://docs.opensafely.org/using-opensafely/viewing-and-releasing-outputs/viewing-and-releasing-with-airlock/how-tos/create-and-submit-a-release-request/)

The table number loosely corresponds to the sections in the [protocol](https://github.com/opensafely/ADHD-Pre-and-Post-Covid/blob/1336ee91b49d90877f221f92d16f00183e47e167/protocol%20/README.md)

## Measures Framework
In this section, all outputs are generated using the [measures framework](https://docs.opensafely.org/ehrql/explanation/measures/) will be subject to the framework's own disclosure control i.e. the author will not no implement own suppression techniques such as functions to round values. The statistics is broken down by the same category age and sex. The timeframe for all tables is each tax year between 2016 to 2025.  

* Table_2_Prevalence_of_ADHD_Diagnosis – The file displays the prevalence including counts of ADHD diagnosis for each year in the general population
* Table_3_with_ADHD_that_are_prescribed_ADHD_medication - The file displays the prevalence including counts of patients with an ADHD diagnosis and taking ADHD medication for each year in the general population
* Table_3_without_ADHD_that_are_prescribed_ADHD_medication - The file displays the prevalence including counts of patients with an ADHD medication and do not have an ADHD diagnosed code in the general population
* Table_3_are_prescribed_ADHD_medication_in_ADHD_group - The file displays the prevalence including counts of patients that have taken ADHD medication in the population of patients of with ADHD diagnosis code.

## User defined outputs
In this section, all outputs are curated by the author

* Table_3_rolling_6_month_medication – The table shows a 6 month rolling cumulative summation count of patients taking ADHD medication at monthly intervals April 2016 to April 2025. The summation counts are broken down by sex and age. Disclosure Control:
    * The age category is grouped at a larger age range in 35 and over to suppress small numbers.
    * The final figure in the rolling_6_month_sum is rounded up by unit of 10.
* Table_5_time_from_diagnosis_to_treatment – Shows the medium and mean time between the first diagnosis date and first medication date. In addition, shows the counts of the population size broken down by age and sex. Disclosure Control:
    * The size figure is rounded up to the near unit of 10.
    * The age category is grouped at a larger age range in 35 and over to suppress small numbers.
    * The minimum size is floored at 20 to avoid possible secondary exposure.
    * The mean and medium of weeks are rounded.