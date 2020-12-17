import os
import pandas as pd
import random
from time import sleep
import user_actions
import data_bases

titles_data_path = '/home/bohdanm/Documents/mini_project_first_semester/sources/author/titles.csv'

main_df = data_bases.make_proper_titles_data(titles_data_path)


all_criterions = ['Name', 'Series title', 'Country of publication', 'Material type',
                  'Place of publication', 'Publisher', 'Genre', 'Languages']


def main():

    user_actions.clear_console()

    user_actions.display(
        'Hellooooooooooooooooofhdsfhjsdfksdhfskdjfskdjhfsdjhskdjooooooooooooooooooooooooooooooooooooooooo')

    user_actions.await_user()

    single_mutiple_value = user_actions.sing_mult()

    user_actions.choices(all_criterions)

    if single_mutiple_value == 1:
        certain_criterions = user_actions.return_single_choice()
    else:
        certain_criterions = user_actions.return_multiple_choice()

    final_croterions = user_actions.subparagraph(main_df, certain_criterions)

    output = data_bases.final_result(main_df, final_croterions)

    return output


if __name__ == "__main__":
    print(main())
