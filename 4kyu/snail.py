# Snail
# URL: https://www.codewars.com/kata/snail


def snail(an_array):
    ret_list = []

    def sub_snail(a_array):
        if len(a_array) == 0 or a_array == [[]]:
            return ret_list
        if len(a_array) == 1:
            ret_list.append(a_array[0][0])
            return ret_list
        for char in a_array[0]:
            ret_list.append(char)
        a_array.pop(0)
        for sub_arr in a_array:
            ret_list.append(sub_arr.pop())
        for i in range(len(a_array[-1])-1, -1, -1):
            ret_list.append(a_array[-1][i])
        a_array.pop()
        for sub_arr in reversed(a_array):
            ret_list.append(sub_arr.pop(0))
        return sub_snail(a_array)
    return sub_snail(an_array)
