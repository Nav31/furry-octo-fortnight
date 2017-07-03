# URL: https://www.codewars.com/kata/valid-braces

def validBraces(string):
    oppostie_dict = {'{': '}', '(': ')', '[': ']'}
    str_len = len(string)
    for i in range(str_len/2):
        if oppostie_dict[string[i]] != string[str_len-i-1:str_len-i]:
            return False
    return True

print(validBraces( "()" ))
print(validBraces( "[(])" ))
# print(validBraces('{}()[]'))