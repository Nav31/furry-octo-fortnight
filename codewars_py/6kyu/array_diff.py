# URL: https://www.codewars.com/kata/array-dot-diff


def array_diff(a, b):
    return_list = []
    for num in a:
        if num not in b:
            return_list.append(num)
    return return_list
