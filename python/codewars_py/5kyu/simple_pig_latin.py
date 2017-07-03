# URL: https://www.codewars.com/kata/simple-pig-latin

def pig_it(text):
    const = 'ay'
    return_str = ""
    text = text.split()
    for word in text:
        return_str += word[1:] + word[0:1]
        if word.isalpha():
            return_str += const + " "
    return return_str.strip()

# Best
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])