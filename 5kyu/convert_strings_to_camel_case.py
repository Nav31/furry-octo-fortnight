import re
def to_camel_case(text):
    text = re.sub(r"-|_", " ", text).split()
    return_string = ""
    for idx, word in enumerate(text):
        if idx > 0:
            return_string += word[:1].upper() + word[1:]
        else:
            return_string += word
    return return_string

# print to_camel_case("the_stealth_warrior")

# Best
def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s