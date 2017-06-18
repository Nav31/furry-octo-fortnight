# URL: https://www.codewars.com/kata/unique-in-order


def unique_in_order(iterable):
    return_list = []
    prev_char = ""
    for letter in iterable:
        if letter != prev_char:
            prev_char = letter
            return_list.append(letter)
    return return_list

# Clever
from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]
