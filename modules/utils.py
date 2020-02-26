from datetime import timedelta, datetime
import pandas as pd

def grouper_UT(df, UTb, UTe):
    '''
    df: df to slice (must be sorted by date)
    UTb: begining UT time of interest
    UTe: end of UT time of interest (next day)

    return: a list of dfs with the slices
    '''
    n_days = (df.index[-1] - df.index[0]).days

    date_0 = df.index.date[0]
    date_f = date_0 + timedelta(days=1)

    date_0 = datetime.combine(date_0, UTb)
    date_f = datetime.combine(date_f, UTe)

    condition = (date_0 < df.index) & (df.index < date_f)
    conditions = [condition]
    conditions += [((date_0 + timedelta(days=i)) < df.index) & (
                df.index < (date_f + timedelta(days=i)))
                   for i in range(n_days)]

    UT_days = [df.loc[single_condition] for single_condition in conditions][1:]  # the first item is repeated


    return UT_days


def list2dict(list_dfs):
    """
    it takes a list of sliced dfs and turns it into a dict with
    the date as key
    :param list_dfs: a list of ut sampled dfs
    :return: a dict of ut sampled dfs
    """

    return {df.index[0].strftime('%Y-%m-%d'): df for df in list_dfs
            if len(df) != 0}



def dic2df(dict_utdf):
    """
    This function takes a dictionary of dfs where the key is the date_key
    and mixes everything into one big df with the ke in a date_key column
    :param dict_utdf: dictionary of timeseries dfs
    :return: pandas dataframe
    """
    list2concat = []
    for date_key in dict_utdf:
        dict_utdf[date_key]['date_key'] = date_key
        list2concat.append(dict_utdf[date_key])
    return pd.concat(list2concat)


def add_dake_key_column(df, UT_interval):
    """
    this function takes a df with datetime index and turns it into a
    df with the date_key as a new column
    :param df: df to add the column
    :param UT_interval: UT inteval to define nights
    :return: pandas df with the new column
    """
    return dic2df(list2dict(grouper_UT(df, *UT_interval)))
