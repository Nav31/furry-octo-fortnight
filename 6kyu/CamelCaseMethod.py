# https://www.codewars.com/kata/camelcase-method/train/python

def camel_case(string):
    return "".join(string.title().split())

print(camel_case("camel case"))