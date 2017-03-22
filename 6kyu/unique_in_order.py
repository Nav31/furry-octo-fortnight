def unique_in_order(iterable):
    previous_char = ""
    return_list = []
    for char in iterable:
        if char != previous_char:
            previous_char = char
            return_list.append(char)
    return return_list