def maxSequence(arr):
    highest = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subArr = arr[i:j+1]
            if sum(subArr) > highest:
                highest = sum(subArr)
    return highest

print maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])