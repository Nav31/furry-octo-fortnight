# https://www.codewars.com/kata/tribonacci-sequence/train/python

def tribonacci(signature, n):
    if n == 0:
        return []
    elif n == 1:
        return [signature[0]]
    elif len(signature) < 3:
        return signature
    else:
        def sum_last_3(a_list):
            return sum(a_list[-3:])
        counter = 0
        while len(signature) < n:
            signature.append(sum_last_3(signature))
            counter += 1
        return signature


def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))
    return res
