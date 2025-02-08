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