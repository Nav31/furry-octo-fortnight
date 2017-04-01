def valid_parentheses(string):
    counter = 0
    for paren in string:
        if paren == "(":
            counter += 1
        elif paren == ')':
            counter -= 1
        if counter < 0:
            return False
    if counter != 0:
        return False
    return True
print valid_parentheses("  (")

# Best
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False