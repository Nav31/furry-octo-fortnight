def pig_it(text):
    ay = 'ay'
    return_str = ""
    for letter in text.split():
        if letter.isalpha():
            return_str += letter[1:] + "".join(letter[0:1]) + ay + ' '
        else:
            return_str += letter
    return return_str.rstrip()

print pig_it('Quis custodiet ipsos custodes ?') #"uisQay ustodietcay psosiay ustodescay ?"

# Best
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
