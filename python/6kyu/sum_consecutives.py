# Sum Consecutives
# URL: https://www.codewars.com/kata/sum-consecutives/train/python


def sum_consecutives(array):
    return_list = []
    sub_sum = None
    for idx, val in enumerate(array[:-1]):
        if val == array[idx+1]:
            if sub_sum:
                sub_sum += val
            else:
                sub_sum = val
        else:
            if sub_sum:
                sub_sum += val
                return_list.append(sub_sum)
                sub_sum = None
            else:
                return_list.append(val)
        if idx+2 == len(array)-1:
            return_list.append(array[idx+1]) if not sub_sum else return_list.append(sub_sum)
    return return_list

# print(sum_consecutives([1,4,4,4,0,4,3,3,1]))    # [1,12,0,4,6,1]
# print(sum_consecutives([1,1,7,7,3]))    # [2,14,3]
# print(sum_consecutives([-5,-5,7,7,12,0]))
# print(sum_consecutives([0, 1, 1, 2, 2]))
print(sum_consecutives([1,2,3,3,4,4]))