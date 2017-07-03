def rotate(arr, n):
    if n < 0:
        for i in range(0, n, -1):
            val = arr.pop(0)
            arr.append(val)
    elif n > 0:
        for i in range(n):
            val = arr.pop()
            arr.insert(0,val)
    else:
        return arr
    return arr
data = [1, 2, 3, 4, 5]
print rotate(data, 2)