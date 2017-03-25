def sum_pairs(ints, s):
    memo = dict()
    for num in ints:
        num2 = s - num
        if num2 in memo:
            return [num2, num]
        else:
            memo[num] = 1













        # temp_num = s - num
        # # print temp_num, num
        # if temp_num in ints and temp_num != num:
        #     return [num, temp_num]
        #     # return_list.append(num)
        #     # return_list.append(s-num)
        #     # return return_list

l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5] #10
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

# print sum_pairs(l1, 8)
# print sum_pairs(l2, -6)

print sum_pairs(l1, 8)
print sum_pairs(l2, -6)
print sum_pairs(l3, -7)
print sum_pairs(l4, 2)
print sum_pairs(l5, 10)
print sum_pairs(l6, 8)
print sum_pairs(l7, 0)
print sum_pairs(l8, 10)