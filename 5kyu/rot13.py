# https://www.codewars.com/kata/rot13-1


def rot13(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # iterate => check if alpha => get current index of letter => add 13 (if greater, wrap around) => append back\
    return_string, is_upper = "", False
    for char in message:
        if char.isupper():
            is_upper = True
            char = char.lower()
        if char.isalpha():
            next_char_idx = alphabet.index(char) + 13
            if next_char_idx > len(alphabet) - 1:
                char = alphabet[next_char_idx % len(alphabet)]
            else:
                char = alphabet[next_char_idx]
        if is_upper:
            char = char.upper()
            is_upper = False
        return_string += char
    return return_string


print(rot13("Test"))