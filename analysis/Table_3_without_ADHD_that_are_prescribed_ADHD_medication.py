from ehrql import INTERVAL, case, create_measures, when, years
from ehrql.tables.tpp import (
    patients,
    practice_registrations,
    clinical_events,
    medications,
)

from codelists import (
    adhd_codelist, 
    adhdrem_codelist,
    adhd_medication_codelist,
    
)

from variables_library import (
    first_matching_event, 
    last_matching_event, 
    event_ADHD,
    first_medication_event,
    first_event_ADHD,
    add_datestamp
)

'''
The following scripts looks at the measure of selected medication used

This is a combination of two groups
1) Patients with medication AND no diagonsis
'''

measures = create_measures()
measures.configure_dummy_data(population_size=1000)

# Population variables
has_registration = practice_registrations.spanning(
    INTERVAL.start_date, INTERVAL.end_date
).exists_for_patient()

sex = patients.sex
age = patients.age_on(INTERVAL.start_date)
age_band = case(
    when((age >= 0) & (age <= 9)).then("0 to 9"),
    when((age >= 10) & (age <= 17)).then("10 to 17"),
    when((age >= 18) & (age <= 24)).then("18 to 24"),
    when((age >= 25) & (age <= 34)).then("25 to 34"),
    when((age >= 35) & (age <= 44)).then("35 to 44"),
    when((age >= 45) & (age <= 54)).then("45 to 54"),
    when((age >= 55) & (age <= 64)).then("55 to 64"),
    when((age >= 65) & (age <= 74)).then("65 to 74"),
    when(age >= 75).then("75 and over"),
    when(age.is_null()).then("Missing"),
)

selected_events = medications.where(
    medications.date.is_on_or_before(INTERVAL.end_date)
)

has_med_date = first_medication_event(selected_events, adhd_medication_codelist).date

selected_conditions = clinical_events.where(
    clinical_events.date.is_on_or_before(INTERVAL.end_date)
)

has_adhd_cod_date = first_matching_event(selected_conditions, adhd_codelist).date

#Computing group 1 - medication and NO diagnosis
has_med_and_no_dia = has_med_date.is_not_null() & (has_adhd_cod_date.is_null())

#This looks at the incidence of ADHD medication in the entire population
measures.define_measure(
    name= f"Table_3_without_ADHD_that_are_prescribed_ADHD_medication" + add_datestamp(),
    numerator= has_med_and_no_dia,
    denominator=(
        has_registration
        & patients.sex.is_in(["male", "female"])
        & (age <= 120)
        & patients.is_alive_on(INTERVAL.end_date)
    ),
    group_by={"sex": sex, "age_band": age_band},
    intervals=years(9).starting_on("2016-04-01"),
)

