
def dig_pow(n ,p):
    # 89 --> 8^1 + 9^2 = 89 * 1
    sum_of_num_list = 0
    num_list = [int(x) for x in list(str(n))]
    for index, num in enumerate(num_list):
        sum_of_num_list += num ** (p+index)
    for i in range(n+3000,0,-1):
        if sum_of_num_list / i == n:
            return i
    return -1

# print dig_pow(46288, 3)
# print dig_pow(89, 1)
print dig_pow(10383, 6)