# URL: https://www.codewars.com/kata/convert-string-to-camel-case/train/python
import re
def to_camel_case(text):
    if text == "":
        return text
    split_str = re.sub(r"-|_", " ", text).split()
    return split_str[0] + "".join([char[0].upper() + char[1:] for char in split_str[1:]])


# Best
def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s