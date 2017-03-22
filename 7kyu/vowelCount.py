def getCount(inputStr):
    num_vowels = 0
    vowelSet = {"A", "E", "I", "O", "U"}
    for letter in inputStr:
        if(letter.upper() in vowelSet):
            num_vowels += 1
    return num_vowels

# Best
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")