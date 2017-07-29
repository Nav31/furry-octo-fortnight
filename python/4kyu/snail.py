# Snail
# URL: https://www.codewars.com/kata/snail


def snail(array):
    return_list = []

    # This is the top array
    for num in array[0]:
        return_list.append()

    # zipped_tup = zip(*array)
    # print array
    # vertical_right_list = list(zipped_tup[-1])
    #
    # # This is the right vertical row
    # return_list.append(vertical_right_list)
    # # This is the bottom array
    # return_list.append(array[-1][:-1])
    #
    # # vertical left list
    # return_list.append(list(zipped_tup[0])[1:])
    # print(return_list)

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]

array2 = [[1,2,3,1],
          [4,5,6,4],
          [7,8,9,7],
          [7,8,9,7]]

print(snail(array2))