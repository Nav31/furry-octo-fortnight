# https://www.codewars.com/kata/number-of-trailing-zeros-of-n

from math import floor, log


def zeros(n):
    if n == 0:
        return 0
    limit = int(floor(log(abs(n), 5))) + 1
    return sum([n/5**x for x in range(1, limit)]) // 1

