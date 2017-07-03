import re
def is_pangram(s):
    s = s.lower()
    set_of_chars = set(re.sub(r'[^a-z]',"",s))
    if len(set_of_chars) == 26:
        return True
    else:
        return False

is_pangram("The quick, brown fox jumps over the lazy dog!")