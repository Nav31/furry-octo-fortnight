def is_isogram(string):
    letterMap = {}
    string = string.lower()
    for letter in string:
        if(letter in letterMap):
            letterMap[letter] += 1
        else: 
            letterMap[letter] = 1
    for v in letterMap:
      if letterMap[v] > 1:
        return False
    return True  


is_isogram('abb')