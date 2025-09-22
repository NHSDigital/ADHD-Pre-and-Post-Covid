> [!IMPORTANT]  
> This page has been redacted to avoid risk linking data. For details see [The NHS England OpenSAFELY COVID-19 service - privacy notice]( https://digital.nhs.uk/coronavirus/coronavirus-covid-19-response-information-governance-hub/the-nhs-england-opensafely-covid-19-service-privacy-notice)
>
> Unredacted version can be found in [NHS Digital GitHub Org](https://github.com/NHSDigital/datascience-seminars/tree/main/All_materials/20250905_Displaying_SNOMED_usage_for_ADHD_Remission_Code)

> [!WARNING]  
> I’m testing the Microsoft copilot AI to document functions – thus treat the docstring with caution


# Displaying the SNOMED usage for the Financial Year 2023 to 2024 for ADHD Remission Code 

The following code extracts the counts of ADHD Remission Code from [NHS England SNOMED Code Usage in Primary Care, 2023-24 publication]( https://digital.nhs.uk/data-and-information/publications/statistical/mi-snomed-code-usage-in-primary-care/2023-24). The information is displayed below.

## Method

### Getting Data
The raw data is downloaded through the following links the [excel file]( https://files.digital.nhs.uk/70/C33DEC/SNOMED_code_usage_2023-24.xlsx)

### Data Munging
We filter to SNOMED codes that corresponds to [ADHD remission code]( https://www.opencodelists.org/codelist/nhsd-primary-care-domain-refsets/adhdrem_cod/20250627/)


## Table
The metadata is [described as]( https://files.digital.nhs.uk/D8/F9D898/SNOMED_code_usage_metadata.xlsx):
* SNOMED_Concept_ID - SNOMED concepts which have been added to a patient record in a general practice system during the reporting period. 
* Description - The fully specified name associated with the SNOMED_Concept_ID on the final day of the reporting period (31 July). 
* Usage - The number of times that the SNOMED_Concept_ID was added into any patient record within the reporting period, rounded to the nearerst 10. Usage of 1 to 4 is displayed as *.

[place_table_here]: #
