from ehrql import (
    INTERVAL, 
    case, 
    create_measures, 
    when, 
    years
)

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

def first_matching_event(events, codelist, where=True):
    """Select the first matching SNOMED CT event from specified codelist

    Args:
        events (e.g., clinical_events or ): Many rows per patient event frame to select first matching event from codelist from
        codelist (codelist): Clinical codelist, must be using snomedct codes
        where (bool, optional): _description_. Defaults to True.

    Returns:
        patient frame: One row per patient frame, with the first matching event from codelist
    """
    return (
        events.where(where)
        .where(events.snomedct_code.is_in(codelist))
        .sort_by(events.date)
        .first_for_patient()
    )

# Helper function for finding the last matching event
def last_matching_event(events, codelist, where=True):
    """Select the last matching SNOMED CT event from specified codelist

    Args:
        events (e.g., clinical_events or ): Many rows per patient event frame to select last matching event from codelist from
        codelist (codelist): Clinical codelist, must be using snomedct codes
        where (bool, optional): _description_. Defaults to True.

    Returns:
        patient frame: One row per patient frame, with the last matching event from codelist
    """
    return (
        events.where(where)
        .where(events.snomedct_code.is_in(codelist))
        .sort_by(events.date)
        .last_for_patient()
    )

def event_ADHD():
    """Creates a ADHD diagonsis under the business rules

    Returns:
        patient frame: One row per patient frame, with the first matching event from codelist
    
    """

    selected_events = clinical_events.where(
    clinical_events.date.is_on_or_before(INTERVAL.end_date)
    )

    has_adhd_cod_date = last_matching_event(selected_events, adhd_codelist).date

    has_adhdrem_cod_date = last_matching_event(selected_events, adhdrem_codelist).date

    # Select patients with a diagnosis of ADHD
    has_adhd_rule_1 = has_adhd_cod_date.is_not_null()

    # Select patients with:
    # (a) no remission code or
    # (b) a new ADHD diagnosis after the most recent remission code
    has_adhd_rule_2 = (has_adhdrem_cod_date.is_null()) | (
        has_adhd_cod_date > has_adhdrem_cod_date
    )

    has_adhd_rule_1_and_2 = has_adhd_rule_1 & has_adhd_rule_2

    return has_adhd_rule_1_and_2