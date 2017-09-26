from math import floor, log


def trailing_zeros(n, base):
    def toStr(n, base):
        convertString = "0123456789ABCDEF"
        if n < base:
            return convertString[n]
        else:
            return toStr(n // base, base) + convertString[n % base]

    if n == 0:
        return 0
    limit = int(floor(log(abs(n), 5))) + 1
    return sum([n/5**x for x in range(1, limit)]) // 1

print(trailing_zeros(15, 10))
print(trailing_zeros(7, 2))