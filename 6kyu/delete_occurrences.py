def delete_nth(order, max_e):
    count_same_num = 1
    for idx, num in enumerate(order):
        for i in range(idx+1, len(order)):
            if num == order[i]:
                count_same_num += 1
                if count_same_num > max_e:
                    order[i] = " "
        count_same_num = 1
    return list(filter(lambda x: x != " ", order))

# print delete_nth([20,37,20,21], 1)
# print delete_nth([1,1,3,3,7,2,2,2,2], 3)

# Best
def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans
    