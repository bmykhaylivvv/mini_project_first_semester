"""Module: data_bases for MINI-PROJECT.
    Functions for with database.  

    Functions
    ---------
        make_proper_titles_data: function makes a dataframe with certain columns
        final_result: function returns dataframe with suitable criterions
"""


import pandas as pd
import random


titles_data_path = '/home/bohdanm/Documents/mini_project_first_semester/sources/author/titles.csv'

lst = ['Title', 'Name', 'Series title', 'Country of publication', 'Material type',
       'Place of publication', 'Publisher', 'Genre', 'Languages']


def make_proper_titles_data(titles_data_path):
    initial_data = pd.read_csv(titles_data_path)
    certain_columns = initial_data[['Title', 'Name', 'Series title', 'Country of publication', 'Material type',
                                    'Place of publication', 'Publisher', 'Genre', 'Languages']]
    return certain_columns


def final_result(df, criterions):
    df1 = df
    for crit in criterions:
        # print(i[0], i[1])
        df1 = df.loc[df[crit[0]] == crit[1]]
    return df1
