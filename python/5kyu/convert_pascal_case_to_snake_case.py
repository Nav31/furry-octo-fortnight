import re
def to_underscore(string):
    if type(string) is not str:
        return str(string)
    title_array = re.findall("[A-Z][^A-Z]*", string)
    title_array = [word.lower() for word in title_array]
    return "_".join(title_array)