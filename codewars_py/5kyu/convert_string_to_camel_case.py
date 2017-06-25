# URL: https://www.codewars.com/kata/convert-string-to-camel-case/train/python
import re
def to_camel_case(text):
    if text == "":
        return text
    split_str = re.sub(r"-|_", " ", text).split()
    return split_str[0] + "".join([char[0].upper() + char[1:] for char in split_str[1:]])

print(to_camel_case(''))
print to_camel_case("the_stealth_warrior")