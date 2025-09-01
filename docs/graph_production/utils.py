import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.ticker as mtick
import matplotlib.transforms as transforms

from config import nhs_palette

def single_year_table(table):
    """
    Transforms the input DataFrame to a pivot table showing 'ratio' values by 'age_band' and 'sex'.

    Parameters:
        table (pd.DataFrame): Input DataFrame containing at least the columns 'ratio', 'sex', and 'age_band'.

    Returns:
        pd.DataFrame: Pivot table with 'age_band' as index, 'sex' as columns, and 'ratio' as values.
    """

    table = table[['ratio','sex','age_band']]
    table = table[~table['ratio'].isnull()]

    table = pd.pivot_table(table, values='ratio', index=['age_band'], columns=['sex'] )

    return table

                            
def grouped_by_demographics(table, demo, cols_to_sum = ['numerator','denominator'], year_col = ['interval_start']):
    """
    Aggregates and summarizes a table by specified demographic and year columns.

    Parameters:
        table (pd.DataFrame): The input DataFrame containing the data to be grouped and summarized.
        demo (str): The name of the demographic column to group by (e.g., 'gender', 'age_group').
        cols_to_sum (list of str, optional): List of column names to sum within each group. 
            Defaults to ['numerator', 'denominator'].
        year_col (list of str, optional): List of column names representing the year or interval to group by.
            Defaults to ['interval_start'].

    Returns:
        pd.DataFrame: A DataFrame grouped by the specified demographic and year columns, 
            with summed values for the specified columns and an additional 'ratio' column 
            representing the percentage (numerator/denominator * 100) for each group.
    """

    #Need to sum over
    combine_cols = year_col + [demo]

    output = table.groupby(combine_cols, as_index = False)[cols_to_sum].sum()

    #Computing the ratio
    output['ratio'] = output[cols_to_sum[0]]/output[cols_to_sum[1]]

    #Covert into percentage
    output['ratio'] = output['ratio']*100

    return output


def grouped_by_overall(table, cols_to_sum = ['numerator','denominator'], year_col = ['interval_start']):
    """
    Groups a pandas DataFrame by specified columns, sums selected columns, and computes a percentage ratio.

    Args:
        table (pd.DataFrame): The input DataFrame containing the data to be grouped and summarized.
        cols_to_sum (list of str, optional): List of column names to sum. The first column is used as the numerator,
            and the second as the denominator for the ratio calculation. Defaults to ['numerator', 'denominator'].
        year_col (list of str, optional): List of column names to group by. Defaults to ['interval_start'].

    Returns:
        pd.DataFrame: A DataFrame grouped by `year_col`, with summed columns in `cols_to_sum` and an additional
            'ratio' column representing the percentage (numerator/denominator * 100).
    """
                            

    #Need to sum over
    combine_cols = year_col

    output = table.groupby(combine_cols, as_index = False)[cols_to_sum].sum()

    #Computing the ratio
    output['ratio'] = output[cols_to_sum[0]]/output[cols_to_sum[1]]

    #Covert into percentage
    output['ratio'] = output['ratio']*100

    return output

def plot_adhd_prevalence_charts(sex_group, age_group_young, age_group_middle, age_group_old, nhs_palette = nhs_palette ):
    """
    Plots ADHD prevalence and count charts by sex and age bands.
    This function creates a 2x2 grid of subplots visualizing ADHD prevalence (as a percentage)
    and counts (as bar plots) over time, split by sex and three age groups (young, middle, old).
    Each subplot contains a line plot for prevalence and a bar plot for counts, with legends
    and axis labels appropriately set.
    Parameters
    ----------
    sex_group : pandas.DataFrame
        DataFrame containing ADHD prevalence and count data grouped by sex. Must include columns:
        'interval_start', 'ratio', 'numerator', 'sex'.
    age_group_young : pandas.DataFrame
        DataFrame containing ADHD prevalence and count data for young age bands. Must include columns:
        'interval_start', 'ratio', 'numerator', 'age_band'.
    age_group_middle : pandas.DataFrame
        DataFrame containing ADHD prevalence and count data for middle age bands. Must include columns:
        'interval_start', 'ratio', 'numerator', 'age_band'.
    age_group_old : pandas.DataFrame
        DataFrame containing ADHD prevalence and count data for old age bands. Must include columns:
        'interval_start', 'ratio', 'numerator', 'age_band'.
    nhs_palette : dict or list, optional
        Color palette to use for the plots. Should be compatible with seaborn's palette argument.
    Returns
    -------
    fig : matplotlib.figure.Figure
        The matplotlib Figure object containing the plots.
    axes : numpy.ndarray
        Array of matplotlib Axes objects for the subplots.
    Notes
    -----
    - Each subplot combines a line plot (prevalence) and a bar plot (counts) with a shared x-axis.
    - Legends are customized to display both prevalence and count information.
    - The function assumes the input DataFrames are properly formatted and indexed.
    """

    
    fig, axes = plt.subplots(2, 2, figsize=(15.7, 15.3))  # A4 landscape in inches

    # By sex
    sns.lineplot(x="interval_start", y="ratio", hue="sex", data=sex_group, ax=axes[0, 0], palette=nhs_palette)
    axes[0, 0].set_ylabel("Prevalence, %")
    axes[0, 0].set_xlabel("Year")
    ax_tmp0 = axes[0, 0].twinx()
    sns.barplot(x="interval_start", y="numerator", hue="sex", ax=ax_tmp0, data=sex_group, palette=nhs_palette, alpha=0.3, dodge=True)
    ax_tmp0.set_ylabel("Count")
    axes[0, 0].set_title("ADHD Prevalence and Counts by Sex")
    axes[0, 0].set_xticklabels(axes[0, 0].get_xticklabels(), rotation=90)
    #axes[0, 0].get_legend().remove()
    handles1, labels1 = axes[0, 0].get_legend_handles_labels()
    handles2, labels2 = ax_tmp0.get_legend_handles_labels()
    axes[0, 0].legend((*handles1, *handles2), (*len(labels1)*[''], *labels2),
             loc='best', ncol=2, handlelength=3, edgecolor='black', handletextpad = 0.1,
             labelspacing = 0.1, columnspacing = 0.1,
             )
    ax_tmp0.get_legend().remove()

    # Young age bands
    sns.lineplot(x="interval_start", y="ratio", hue="age_band", data=age_group_young, ax=axes[0, 1], palette=nhs_palette)
    axes[0, 1].set_ylabel("Prevalence, %")
    axes[0, 1].set_xlabel("Year")
    ax_tmp1 = axes[0, 1].twinx()
    sns.barplot(x="interval_start", y="numerator", hue="age_band", ax=ax_tmp1, data=age_group_young, palette=nhs_palette, alpha=0.3, dodge=True)
    ax_tmp1.set_ylabel("Count")
    axes[0, 1].set_title("ADHD Prevalence and Counts by Age Band (Young)")
    axes[0, 1].set_xticklabels(axes[0, 1].get_xticklabels(), rotation=90)
    #axes[0, 0].get_legend().remove()
    handles1, labels1 = axes[0, 1].get_legend_handles_labels()
    handles2, labels2 = ax_tmp1.get_legend_handles_labels()
    axes[0, 1].legend((*handles1, *handles2), (*len(labels1)*[''], *labels2),
             loc='best', ncol=2, handlelength=3, edgecolor='black',handletextpad = 0.1,
             labelspacing = 0.1, columnspacing = 0.1
             )
    ax_tmp1.get_legend().remove()

    # Middle age bands
    sns.lineplot(x="interval_start", y="ratio", hue="age_band", data=age_group_middle, ax=axes[1, 0], palette=nhs_palette)
    axes[1, 0].set_ylabel("Prevalence, %")
    axes[1, 0].set_xlabel("Year")
    ax_tmp2 = axes[1, 0].twinx()
    sns.barplot(x="interval_start", y="numerator", hue="age_band", ax=ax_tmp2, data=age_group_middle, palette=nhs_palette, alpha=0.3, dodge=True)
    ax_tmp2.set_ylabel("Count")
    axes[1, 0].set_title("ADHD Prevalence and Counts by Age Band (Middle Age)")
    axes[1, 0].set_xticklabels(axes[1, 0].get_xticklabels(), rotation=90)

    handles1, labels1 = axes[1, 0].get_legend_handles_labels()
    handles2, labels2 = ax_tmp2.get_legend_handles_labels()
    axes[1, 0].legend((*handles1, *handles2), (*len(labels1)*[''], *labels2),
             loc='best', ncol=2, handlelength=3, edgecolor='black',handletextpad = 0.1,
             labelspacing = 0.1, columnspacing = 0.1
             )
    ax_tmp2.get_legend().remove()

    # Old age bands
    sns.lineplot(x="interval_start", y="ratio", hue="age_band", data=age_group_old, ax=axes[1, 1], palette=nhs_palette)
    axes[1, 1].set_ylabel("Prevalence, %")
    axes[1, 1].set_xlabel("Year")
    ax_tmp3 = axes[1, 1].twinx()
    sns.barplot(x="interval_start", y="numerator", hue="age_band", ax=ax_tmp3, data=age_group_old, palette=nhs_palette, alpha=0.3, dodge=True)
    ax_tmp3.set_ylabel("Count")
    axes[1, 1].set_title("ADHD Prevalence and Counts by Age Band (Retired)")
    axes[1, 1].set_xticklabels(axes[1, 1].get_xticklabels(), rotation=90)
    handles1, labels1 = axes[1, 1].get_legend_handles_labels()
    handles2, labels2 = ax_tmp3.get_legend_handles_labels()
    axes[1, 1].legend((*handles1, *handles2), (*len(labels1)*[''], *labels2),
             loc='best', ncol=2, handlelength=3, edgecolor='black',handletextpad = 0.1,
             labelspacing = 0.1, columnspacing = 0.1
             )
    ax_tmp3.get_legend().remove()

    plt.tight_layout()

    #plt.subplots_adjust(hspace=1.75)
    return fig, axes

def get_sex_and_age_groups(table):
    """
    Groups the input table by sex and age bands, and further splits age groups into young, middle, and old categories.

    Args:
        table (pd.DataFrame): The input DataFrame containing demographic data with 'sex' and 'age_band' columns.

    Returns:
        tuple: A tuple containing:
            - sex_group (pd.DataFrame): Data grouped by 'sex'.
            - age_group (pd.DataFrame): Data grouped by 'age_band'.
            - age_group_young (pd.DataFrame): Data for age bands '0 to 9', '10 to 17', '18 to 24'.
            - age_group_middle (pd.DataFrame): Data for age bands '25 to 34', '35 to 44', '45 to 54', '55 to 64'.
            - age_group_old (pd.DataFrame): Data for age bands '65 to 74', '75 and over'.
    """
    sex_group = grouped_by_demographics(table, 'sex')
    age_group = grouped_by_demographics(table, 'age_band')
    age_group_young = age_group[age_group['age_band'].isin(['0 to 9', '10 to 17', '18 to 24'])]
    age_group_middle = age_group[age_group['age_band'].isin(['25 to 34', '35 to 44', '45 to 54', '55 to 64'])]
    age_group_old = age_group[age_group['age_band'].isin(['65 to 74', '75 and over'])]
    return sex_group, age_group, age_group_young, age_group_middle, age_group_old


def watermark_plot(axes, watermark_string):
    """
    Adds a watermark text to each subplot in the given axes.

    Parameters
    ----------
    axes : numpy.ndarray or matplotlib.axes.Axes
        An array of matplotlib Axes objects or a single Axes object to which the watermark will be added.
    watermark_string : str
        The text to be used as the watermark.

    Returns
    -------
    axes : numpy.ndarray or matplotlib.axes.Axes
        The axes with the watermark text added to each subplot.
    """

    for ax in axes.flat:
        ax.text(
            0.5, 0.5, watermark_string,
            transform=ax.transAxes,
            fontsize=50, color='gray', alpha=0.5,
            ha='center', va='center', rotation=30
        )
    return axes
    

