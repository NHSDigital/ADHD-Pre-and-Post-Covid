from datetime import (
    datetime
)

def add_datestamp():
    """Getting a time stamp link

    Returns:
        datetime_string : string of date string
    """
    datetime_string = datetime.today().strftime('%d_%m_%Y_%H_%M')

    return datetime_string