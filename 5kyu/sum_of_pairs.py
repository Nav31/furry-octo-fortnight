def sum_pairs(ints, s):
    memo = dict()
    for num in ints:
        num2 = s - num
        if num2 in memo:
            return [num2, num]
        else:
            memo[num] = 1