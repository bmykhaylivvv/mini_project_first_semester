import pandas as pd
import random

titles_data_path = '/home/bohdanm/Documents/mini_project_first_semester/sources/author/titles.csv'

lst = ['Name', 'Series title', 'Country of publication', 'Material type',
       'Place of publication', 'Publisher', 'Genre', 'Languages']


def make_proper_titles_data(titles_data_path):
    initial_data = pd.read_csv(titles_data_path)
    certain_columns = initial_data[['Name', 'Series title', 'Country of publication', 'Material type',
                                    'Place of publication', 'Publisher', 'Genre', 'Languages']]
    return certain_columns


def random_choice(num_lst, single_or_multiple):
    lst = ['Name', 'Series title', 'Country of publication', 'Material type',
           'Place of publication', 'Publisher', 'Genre', 'Languages']    

    if single_or_multiple == 1:
        rand_num = random.choice(num_lst)
        return {lst[rand_num]}

    rndm_lst = random.sample(num_lst, 3)
    output = {lst[rndm_lst[0]], lst[rndm_lst[1]], lst[rndm_lst[2]]}

    return output


df = make_proper_titles_data(titles_data_path)
criterions = random_choice([0, 1, 2, 3, 4, 5, 6, 7], 3)

def subparagraph(df, criterions: list):
    """
    Тут юзеру обов'язково потрібно обрати по чому він хоче сортувати, потім доробимо функціб так, 
    щоб можна було вибрати по всіх критеріях в множині
    """
    output = []
    for criter in criterions:
        print(f'Choose values to sort in this cathegory: {criter} \n')
        category_st = set(df[criter].unique())
        print(category_st)
        while True:

            value = input('Enter value to sort: ')
            if value == '':
                break
            elif value in category_st:
                to_append = (criter, value)
                output.append(to_append)
                break
            else:
                print('Enter category from list')
        print('_______________________________________________________')

    return output

def final_result(df, criterions):
    # Дописати умову, для пустих списків
    df1 = df
    for crit in criterions:
        # print(i[0], i[1])
        df1 = df.loc[df[crit[0]] == crit[1]]
    return df1


crittt = subparagraph(df, criterions)

print(final_result(df, crittt))

















# print(df.columns)
# print(df.loc['Name'])
# print(set(df['Name'].unique()))
# print(set(df['Name']))

