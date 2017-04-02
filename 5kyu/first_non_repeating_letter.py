def first_non_repeating_letter(string):
    case_sensative_str = string.lower()
    letter_map = dict()
    lowest_index = len(string) - 1
    all_repeating_chars = True
    for letter in case_sensative_str:                       # populate dict. with letter freq
        if letter in letter_map:
            letter_map[letter] += 1
        else:
            letter_map[letter] = 1
    for key, value in letter_map.items():                   # if letter occurs once, find index, see if it has the lowest index
        if value == 1:
            all_repeating_chars = False
            idx = case_sensative_str.find(key)
            if idx < lowest_index:
                lowest_index = idx                          # if so, set lowest_index to idx
    if all_repeating_chars:
        return ""
    else:
        return string[lowest_index:lowest_index+1]

# Best
def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]
    return ""