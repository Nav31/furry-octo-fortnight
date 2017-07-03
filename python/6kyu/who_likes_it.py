def likes(names):
    namesLength = len(names)
    if(namesLength >= 4):
        return "%s, %s and %s others like this" % (names[:1][0], names[1:2][0], namesLength-2)
    elif(namesLength == 3):
        return "%s, %s and %s like this" % (names[:1][0], names[1:2][0], names[2:][0])
    elif(namesLength == 2):
        return "%s and %s like this" % (names[:1][0], names[1:2][0])
    elif(namesLength == 1):
        return "%s likes this" % (names[:1][0])
    else:
        return "no one likes this"

print(likes(['Alex', 'Jacob', 'Mark', 'Max']))

# Best
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)