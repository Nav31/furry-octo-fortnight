def get_middle(s):
    isOdd = False
    if(len(s) % 2 != 0):
        isOdd = True
    if(isOdd):
        return s[(len(s)//2):(len(s)//2)+1]
    else:
        return s[(len(s)/2)-1:(len(s)/2)+1]

def get_middle(s):
       return s[(len(s)-1)/2:len(s)/2+1]

# print(get_middle("test"))
# print(get_middle("testing"))
# print(get_middle("middle"))
# print(get_middle("A"))
# print(get_middle("of"))