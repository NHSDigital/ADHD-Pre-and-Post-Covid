from datetime import (
    datetime
)
import pandas as pd
from dateutil import relativedelta


def add_datestamp():
    """Getting a time stamp link

    Returns:
        datetime_string : string of date string
    """
    datetime_string = datetime.today().strftime('%d_%m_%Y_%H_%M')

    return datetime_string

def monthly_interval_list(start_date, end_date):
    """
    Generates a list of dates at monthly intervals between two dates, inclusive.
    Args:
        start_date (datetime.date or datetime.datetime): The starting date of the interval.
        end_date (datetime.date or datetime.datetime): The ending date of the interval.
    Returns:
        list: A list of dates representing the start of each month from start_date to end_date, inclusive.
    Example:
        >>> from datetime import date
        >>> monthly_interval_list(date(2023, 1, 1), date(2023, 4, 1))
        [datetime.date(2023, 1, 1), datetime.date(2023, 2, 1), datetime.date(2023, 3, 1), datetime.date(2023, 4, 1)]
    """
    
    #Differnce in months
    delta = relativedelta.relativedelta(end_date, start_date)

    res_months = delta.months + (delta.years * 12)

    interval_array = [start_date + relativedelta.relativedelta(months=each_month) for each_month in range(res_months+1)]

    return interval_array


def rolling_6_month_sum(
    dataframe,
    date_column = 'last_mph_med_date_month_date',
    count_column = 'size',
    column_group = ['age_band','sex'],
    rolling_col_name = 'rolling',
    ):

    """
    Calculates a 6-month rolling sum for a specified count column in a DataFrame, grouped by specified columns and date.
    Parameters:
        dataframe (pd.DataFrame): The input DataFrame containing the data.
        date_column (str, optional): The name of the column containing date values. Defaults to 'last_mph_med_date_month_date'.
        count_column (str, optional): The name of the column containing the counts to sum. Defaults to 'size'.
        column_group (list of str, optional): List of column names to group by. Defaults to ['age_band', 'sex'].
        rolling_col_name (str, optional): The name of the output column for the rolling sum. Defaults to 'rolling'.
    Returns:
        pd.DataFrame: A DataFrame with the original group columns, date column, count column, and a new column containing the 6-month rolling sum for each group.
    Notes:
        - Missing dates in the time series are filled with zeros before calculating the rolling sum.
        - The rolling sum uses a window of 6 months with a minimum of 1 period.
    """
    #Need to get inputs
    date_interval = [min(dataframe[date_column]), max(dataframe[date_column])]
    unqiue_combination = dataframe[column_group].drop_duplicates(subset=column_group)

    list_of_dates = monthly_interval_list(date_interval[0], date_interval[1])
    list_of_dates.sort()

    #Create an empty dataframe with the dates
    rolling_template = pd.DataFrame( {date_column:list_of_dates})

    output_table_with_rolling = pd.DataFrame() 

    #Need to get the vaules of each 
    for each_index in unqiue_combination.index:

        each_conbination = unqiue_combination.loc[[each_index],:]

        each_conbination_dict = each_conbination.to_dict('records')[0]

        # Getting the filtered vaules - Source: https://stackoverflow.com/questions/34157811/filter-a-pandas-dataframe-using-values-from-a-dict
        filtred_group = dataframe.loc[(dataframe[list(each_conbination_dict)] == pd.Series(each_conbination_dict)).all(axis=1)]

        #This is to for the join
        cobination_to_join = filtred_group[[date_column,count_column]]

        #This is join and fill in the missing vaule
        each_roll = rolling_template.merge(
            cobination_to_join,
            how='left',
            left_on=date_column,
            right_on=date_column
        ).fillna(0)

        #Sort 
        each_roll = each_roll.sort_values(by=date_column)

        #Need to the 6 month rolling
        each_roll[rolling_col_name] = each_roll[count_column].rolling(6,min_periods = 1).sum()

        # Add back the columns and values from each_conbination to each_roll
        for col in each_conbination.columns:
            each_roll[col] = each_conbination.iloc[0][col]

        # Concatenate each_roll into empty_df
        output_table_with_rolling = pd.concat([output_table_with_rolling, each_roll], ignore_index=True)

    return output_table_with_rolling