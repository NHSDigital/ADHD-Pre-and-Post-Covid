from ehrql import create_dataset, codelist_from_csv
from ehrql.tables.tpp import patients, practice_registrations, clinical_events, medications

# Codelists
adhd_codelist = codelist_from_csv("codelists/nhsd-primary-care-domain-refsets-adhd_cod.csv", column="code")
methylphenidate_codelist = codelist_from_csv("codelists/nhsd-primary-care-domain-refsets-adhd_cod.csv", column="code")

dataset = create_dataset()
dataset.configure_dummy_data(population_size=10000)

# Date range
start_date = f"2016-01-01"
end_date = f"2023-12-31"

# Population variables
was_registered = practice_registrations.for_patient_on(
    start_date
).exists_for_patient() & practice_registrations.for_patient_on(
    end_date
).exists_for_patient()

is_female_or_male = patients.sex.is_in(["female", "male"])

was_adult = (patients.age_on(start_date) >= 18) & (
    patients.age_on(start_date) <= 120
)

was_alive = (
    patients.date_of_death.is_after(end_date)
    | patients.date_of_death.is_null()
)

had_adhd_event = clinical_events.where(
    clinical_events.snomedct_code.is_in(adhd_codelist)
    & clinical_events.date.is_on_or_between(
        start_date, end_date
    )
).exists_for_patient()

dataset.define_population(
                        is_female_or_male
                        & was_adult
                        & was_alive
                        & was_registered
                        & had_adhd_event
                    )


# Exposure variables
years = list(range(2016, 2023 + 1))
# Iterate over each year and set the attribute on the dataset
for year in years:
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    
    # Construct the attribute name dynamically for each year
    attribute_name = f"num_adhd_events_{year}"
    
    # Calculate the number of ADHD events for the given year
    num_adhd_events_year = clinical_events.where(
        clinical_events.snomedct_code.is_in(adhd_codelist)
        & clinical_events.date.is_on_or_between(start_date, end_date)
    ).count_for_patient()
    
    # Set the attribute on the dataset
    setattr(dataset, attribute_name, num_adhd_events_year)


dataset.sex = patients.sex
dataset.dob = patients.date_of_birth