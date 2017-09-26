# https://www.codewars.com/kata/persistent-bugger/train/python

def persistence(n):
    def convert_to_single(num):
        return [int(x) for x in list(str(num))]
    result, counter = n, 0
    while len(str(result)) != 1:
        numb_list = convert_to_single(result)
        result = reduce(lambda x, y: x*y, numb_list)
        counter += 1
    return counter

print(persistence(39))
print(persistence(4))
print(persistence(25))
print(persistence(999))