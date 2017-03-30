def maxSequence(arr):
    highest = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subArr = arr[i:j+1]
            if sum(subArr) > highest:
                highest = sum(subArr)
    return highest
# print maxSequence([21, -6, -21, -22, 7, -28, 30, -13, 27, -13, 21, 23, -10, -13, -28, -6, 13, 21, 27, -24, 8, 9, 0, -30, -1, -27, -21, -18, -3, -25, -23, 8, -3, 12, -22, -14, 25, -29, 24, -19, 23, -14, -11, -30, 22, 12, -12, 30, 19, 20])
print maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])