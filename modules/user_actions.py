"""
Module documentation
"""
import os
import random
from time import sleep

BOLD_TEXT = '\033[1m'  # code for bold text formatting
NORMAL_TEXT = '\033[0m'  # code for normal text formatting
DISPLAY_DELAY = 0.003  # time delay between characters while displaying them in console

lst = ['Title', 'Name', 'Series title', 'Country of publication', 'Material type',
       'Place of publication', 'Publisher', 'Genre', 'Languages']


def format_bold(text: str) -> str:
    """
    Format text so that it looks bold in the console.
    >>> format_bold('some text')
    '\\x1b[1msome text\\x1b[0m'
    >>> format_bold('my text')
    '\\x1b[1mmy text\\x1b[0m'
    >>> format_bold('blah blah blah')
    '\\x1b[1mblah blah blah\\x1b[0m'
    """
    return BOLD_TEXT + text + NORMAL_TEXT


def display(text: str) -> None:
    """
    Display a chunk of text in console letter-by-letter with a certain delay.
    """
    for char in text:
        print(char, end='', flush='True')
        sleep(DISPLAY_DELAY)

    # move to the next line
    print()


def await_user() -> None:
    """
    Wait until user presses Enter.
    """
    #  bold textu don't get the same me twice ha ha
    print(format_bold('Press ENTER to continue!'))
    input()


def clear_console() -> None:
    """
    Clear the console.
    """
    #  for WINDOWS (os.name is 'nt') | for MAC and LINUX (os.name is 'posix')
    os.system('cls' if os.name == 'nt' else 'clear')


def random_choice(num_lst, single_or_multiple):
    """
    Якщо 'single_or_multiple' = 1, то повернеться множина з одним елементон, 
    при будь-яких інших значення -- повернеться множина з трьох (3) значень
    """
    lst = ['Name', 'Series title', 'Country of publication', 'Material type',
           'Place of publication', 'Publisher', 'Genre', 'Languages']

    if single_or_multiple == 1:
        rand_num = random.choice(num_lst)
        return {lst[rand_num]}

    rndm_lst = random.sample(num_lst, 3)
    output = {lst[rndm_lst[0]], lst[rndm_lst[1]], lst[rndm_lst[2]]}

    return output

# print(random_choice([0, 1, 2, 3, 4, 5, 6, 7], 2))


def choices(lst):
    """
    Function return list of available criterions
    >>> lst = ['0', '1', '2', '3', '4', '5', '6', '7']
    >>> 
    """
    # Почистити консоль
    print('Choose one for writing, you want to get: \n')
    for index, criterion in enumerate(lst):
        print(index, criterion)
    print()


def sing_mult():
    print('Choose type of sort')
    print('1 - Single choice')
    print('2 - Multiple choice')
    while True:
        num = input('Enter type from list above: ')
        if num == '1' or num == '2':
            return int(num)
        continue


def return_single_choice():
    """
    Documentation
    """

    lst = ['Name', 'Series title', 'Country of publication', 'Material type',
           'Place of publication', 'Publisher', 'Genre', 'Languages']

    available_values = ['0', '1', '2', '3', '4', '5', '6', '7']

    # criterion = input('Enter number of criterion: ')
    while True:
        criterion = input(f'Enter criterion (you can write inpur for random criterions): ')
        if criterion == 'random':
            return random_choice([0, 1, 2, 3, 4, 5, 6, 7], 1)
        elif criterion not in available_values:
            print('Enter correct form')
        else:
            return [lst[int(criterion)]]


# a = return_single_choice()
# print(a)


def return_multiple_choice(available_values=['0', '1', '2', '3', '4', '5', '6', '7'], i=1, lst=[]):
    """
    Documentation
    """
    criterions_lst = ['Name', 'Series title', 'Country of publication', 'Material type',
                      'Place of publication', 'Publisher', 'Genre', 'Languages']

    lst = []
    # available_values = ['0', '1', '2', '3', '4', '5', '6', '7']
    while len(lst) < 3:
        criterion = input(f'Enter criterion (you can write inpur for random criterions): ')
        if criterion == 'random':
            return random_choice([0, 1, 2, 3, 4, 5, 6, 7], 2)
        if criterion in available_values:
            lst.append(criterion)
        else:
            print('Enter correct form')
        i += 1
        # make integers in list using map
    integer_lst = list(map(lambda element: int(element), lst))
    output_lst = [criterions_lst[integer_lst[0]],
                  criterions_lst[integer_lst[1]], criterions_lst[integer_lst[2]]]
    # В подальшому ретурнити множину, бо юзер може ввести однакові дані

    return output_lst


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


# choices(lst)
# a = return_multiple_choice()
# print(a)
lst = ['0', '1', '2', '3', '4', '5', '6', '7']

# print(random_choice(lst, ''))
# print(return_multiple_choice(['0', '1', '2', '3', '4', '5', '6', '7']))


# a = sing_mult()

# print(random_choice([0, 1, 2, 3, 4, 5, 6, 7], a))
