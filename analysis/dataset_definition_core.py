from ehrql import create_dataset
from ehrql.tables.tpp import (
    patients,
    practice_registrations,
    clinical_events,
    medications,
)

from codelists import adhd_codelist, methylphenidate_codelist

dataset = create_dataset()
dataset.configure_dummy_data(population_size=10)

# Date range
start_date = "2016-01-01"
end_date = "2023-12-31"

# Population variables
has_registration = practice_registrations.spanning(
    start_date, end_date
).exists_for_patient()
dataset.sex = patients.sex
dataset.age = patients.age_on(start_date)

selected_events = clinical_events.where(
    clinical_events.date.is_on_or_between(start_date, end_date)
)

selected_medications = medications.where(
    medications.date.is_on_or_between(start_date, end_date)
)

dataset.has_adhd_event = selected_events.where(
    clinical_events.snomedct_code.is_in(adhd_codelist)
).exists_for_patient()

dataset.has_mph_med = selected_medications.where(
    medications.dmd_code.is_in(methylphenidate_codelist)
).exists_for_patient()

dataset.define_population(
    has_registration
    & dataset.sex.is_in(["male", "female"])
    & (dataset.age >= 18)
    & (dataset.age <= 120)
    & patients.is_alive_on(start_date),
)
