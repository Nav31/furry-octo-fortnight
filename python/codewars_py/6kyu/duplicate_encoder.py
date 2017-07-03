# URL: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

def duplicate_encode(word):
    word = list(word.lower())
    return_str = ""
    for letter in word:
        if word.count(letter) > 1:
            return_str += ")"
        else:
            return_str += "("
    return return_str

# Best
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
