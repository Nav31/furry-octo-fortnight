def toJadenCase(string):
    returnString = ""
    for word in string.split():
        returnString += word[0:1].upper() + word[1:] + " "
    return returnString.strip()

quote = "How can mirrors be real if our eyes aren't real"
print(toJadenCase(quote))

# Best Answer
def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())
