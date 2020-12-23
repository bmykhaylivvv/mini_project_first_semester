"""Module: main for MINI-PROJECT.
    Main module of the project.  
"""
import os
import pandas as pd
import random
from time import sleep
import user_actions
import data_bases
from pathlib import Path


titles_data_path = Path('./data/titles.csv')


main_df = data_bases.make_proper_titles_data(titles_data_path)


all_criterions = ['Name', 'Series title', 'Country of publication', 'Material type',
                  'Place of publication', 'Publisher', 'Genre', 'Languages']


def main():

    user_actions.clear_console()

    user_actions.display(user_actions.format_bold(
        '                                  Christina Georgina Rossetti'))
    user_actions.display(user_actions.format_bold(
        '                               (5 December 1830 – 29 December 1894)'))
    user_actions.show_plot()
    user_actions.await_user()
    single_mutiple_value = user_actions.sing_mult()

    user_actions.choices(all_criterions)

    if single_mutiple_value == 1:
        certain_criterions = user_actions.return_single_choice()
    else:
        certain_criterions = user_actions.return_multiple_choice()

    final_croterions = user_actions.subparagraph(main_df, certain_criterions)

    output = data_bases.final_result(main_df, final_croterions)
    print()

    final_outp = output[['Title', 'Material type', 'Languages', 'Genre',
                         'Series title', 'Country of publication', 'Publisher', 'Place of publication']]

    books_num = user_actions.number_of_books()

    if len(output) >= books_num:
        print(user_actions.format_bold(
            f'Here are {books_num} books which suit your criterions'), end='\n\n')
    else:
        print(user_actions.format_bold(
            f'Here are {len(output)} books which suit your criterions'), end='\n\n')
    return final_outp.head(books_num)


if __name__ == "__main__":
    print(main())
