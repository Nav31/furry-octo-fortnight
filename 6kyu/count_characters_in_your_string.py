def count(string):
    string_count_dict = dict()
    for letter in string:
        if letter in string_count_dict:
            string_count_dict[letter] += 1
        else:
            string_count_dict[letter] = 1
    return string_count_dict
