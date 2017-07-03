# URL: https://www.codewars.com/kata/bit-counting/train/python


def countBits(n):
    bin_num = "{0:b}".format(n)
    return len([x for x in bin_num if x == "1"])


# Best
def countBits(n):
    return bin(n).count("1")