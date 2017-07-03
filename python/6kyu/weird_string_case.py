def to_weird_case(string):
    return_string = ""
    string = string.split()
    for word in string:
        for index, char in enumerate(word):
            print index, char
            if index % 2 == 0:
                return_string += char.upper()  
            else:
                return_string += char
        return_string += " "
    return return_string.rstrip()

print to_weird_case('This is a test')

# Best
def to_weird_case_word(string):
    return "".join(c.upper() if i%2 == 0 else c for i, c in enumerate(string.lower()))
    
def to_weird_case(string):
    return " ".join(to_weird_case_word(str) for str in string.split())