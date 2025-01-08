from ehrql import INTERVAL, case, create_measures, when, years
from ehrql.tables.tpp import (
    patients,
    practice_registrations,
    clinical_events,
    medications,
)

from codelists import adhd_codelist, methylphenidate_codelist

measures = create_measures()
measures.configure_dummy_data(population_size=10)

# Population variables
has_registration = practice_registrations.spanning(
    INTERVAL.start_date, INTERVAL.end_date
).exists_for_patient()

sex = patients.sex
age = patients.age_on(INTERVAL.start_date)
age_band = case(
    when((age >= 0) & (age < 20)).then("0-19"),
    when((age >= 20) & (age < 40)).then("20-39"),
    when((age >= 40) & (age < 60)).then("40-59"),
    when((age >= 60) & (age < 80)).then("60-79"),
    when(age >= 80).then("80+"),
    when(age.is_null()).then("Missing"),
)

selected_events = clinical_events.where(
    clinical_events.date.is_on_or_between(INTERVAL.start_date, INTERVAL.end_date)
)

selected_medications = medications.where(
    medications.date.is_on_or_between(INTERVAL.start_date, INTERVAL.end_date)
)

has_adhd_event = selected_events.where(
    clinical_events.snomedct_code.is_in(adhd_codelist)
).exists_for_patient()

measures.define_measure(
    name=f"adhd_prevalence",
    numerator=has_adhd_event,
    denominator=(
        has_registration
        & patients.sex.is_in(["male", "female"])
        & (age >= 18)
        & (age <= 120)
        & patients.is_alive_on(INTERVAL.start_date)
    ),
    group_by={"sex": sex, "age_band": age_band},
    intervals=years(7).starting_on("2016-01-01"),
)
