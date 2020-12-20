"""Module: user_actions for MINI-PROJECT.
    Functions for interaction with user.  

    Functions
    ---------
        format_bold: make text bold
        display: print a chunk of text in console letter-by-letter with a certain delay
        await_user: wait until user presses Enter
        clear_console: clear the console
        show_plot: show plot in console
        random_choice: return list with random criterions
        choices: print all available criterions
        sing_mult: wait until user choose one of types of sort
        return_single_choice: return list with one criterion
        return_multiple_choice: return list with three criterions
        subparagraph: function returns lis with of values choose by user from certain criterions
        number_of_books: function gets and returns books number for output 
        
"""
import os
import random
from time import sleep
from pathlib import Path
from numbers import Number
import doctest
PLOT_FILE = Path('./docs/plot.txt')  # path to game plot
BOLD_TEXT = '\033[1m'  # code for bold text formatting
NORMAL_TEXT = '\033[0m'  # code for normal text formatting
DISPLAY_DELAY = 0.001  # time delay between characters while displaying them in console

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


def show_plot() -> None:
    """
    Display the plot of the game in the console and
    clears it after user has pressed any key.
    """
    with open(PLOT_FILE, 'r', encoding='utf-8') as plot_file:
        display(plot_file.read())


def random_choice(num_lst: list, single_or_multiple: Number) -> list:
    """
    Function returns list with 1 random element from lst list, if'single_or_multiple' = 1,
    function returns list with 3 random elements from lst list, if 'single_or_multiple' != 1.
    >>> random.seed(1)
    >>> random_choice([1, 2, 3, 4, 5, 6, 7, 8, 9], 1)
    {'Country of publication'}
    >>> len(random_choice([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))
    3
    """
    lst = ['Name', 'Series title', 'Country of publication', 'Material type',
           'Place of publication', 'Publisher', 'Genre', 'Languages']

    if single_or_multiple == 1:
        rand_num = random.choice(num_lst)
        return {lst[rand_num-1]}

    rndm_lst = random.sample(num_lst, 3)
    output = {lst[rndm_lst[0]], lst[rndm_lst[1]], lst[rndm_lst[2]]}

    return output

# print(random_choice([0, 1, 2, 3, 4, 5, 6, 7], 2))


def choices(lst):
    """
    Function print list of available criterion with index ahead
    r>>> choices(['Title', 'Name', 'Series title', 'Country of publication', 'Material type',\
       'Place of publication', 'Publisher', 'Genre', 'Languages'])
        Choose criteion(s) for filter author`s works: 

    0 Title
    1 Name
    2 Series title
    3 Country of publication
    4 Material type
    5 Place of publication
    6 Publisher
    7 Genre
    8 Languages
    """
    clear_console()
    print(format_bold('Choose criteion(s) for filter author`s works: \n'))
    for index, criterion in enumerate(lst):
        print(index, criterion)
    print()


def sing_mult() -> Number:
    """
    Function wait while user enter type of sort
    1 - Single choice
    2 - Multiple choice (3 criterions)
    """
    print(format_bold('Choose type of sort'))
    print('1 - Single choice')
    print('2 - Multiple choice (3 criterions)')
    print()
    while True:
        num = input('Enter type from list above: ')
        if num == '1' or num == '2':
            return int(num)
        continue


def return_single_choice() -> list:
    """
    Function wait while user enter number of criterion and return list with this (only one) criterion.
    User can input 'random' and function return list with one random criterion.
    """

    lst = ['Name', 'Series title', 'Country of publication', 'Material type',
           'Place of publication', 'Publisher', 'Genre', 'Languages']

    available_values = ['0', '1', '2', '3', '4', '5', '6', '7']

    # criterion = input('Enter number of criterion: ')
    while True:
        criterion = input(
            f'Enter criterion (you can write \'random\' for random criterions): ')
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
    Function wait while user enter number of criterion and return list with these criterions.
    User can input 'random' and function return random list of criterions.
    """
    criterions_lst = ['Name', 'Series title', 'Country of publication', 'Material type',
                      'Place of publication', 'Publisher', 'Genre', 'Languages']

    lst = []
    # available_values = ['0', '1', '2', '3', '4', '5', '6', '7']
    while len(lst) < 3:
        criterion = input(
            f'Enter criterion (you can write inpur for random criterions): ')
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
    Function print set with all available choices to sort in choosen criterions.
    Function returns list of values from criterions.
    """
    output = []
    for criter in criterions:
        print()
        print(
            f'Choose values to sort in this cathegory: {format_bold(criter)}\n')
        print(format_bold('You can press Enter to skip this choice\n'))
        category_st = set(df[criter].unique())
        print(category_st)
        while True:
            print()
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


def number_of_books() -> Number:
    """
    Function gets number of how many books user wants to get.
    """
    while True:
        books_number = input('How many books do you want to get? ')
        try:
            books_number = int(books_number)
            assert books_number > 0
            print()  # new line
            return books_number

        except (ValueError, AssertionError) as er:
            continue


doctest.testmod()
