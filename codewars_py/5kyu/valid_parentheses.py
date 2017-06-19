# URL: https://www.codewars.com/kata/valid-parentheses


def valid_parentheses(string):
    counter = 0
    for char in string:
        if char == "(":
            counter += 1
        elif char == ')':
            counter -= 1
        if counter < 0:
            return False
    if counter != 0:
        return False
    return True


# Best
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False