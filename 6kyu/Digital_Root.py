def digital_root(n):
    if (len(str(n)) > 1):
        counter = 0
        listNums = map(int, str(n))
        for num in listNums:
            counter += num
        if(len(str(counter)) > 1):
            return digital_root(counter)
        else:
            return counter
    else:
        return n

# print(digital_root(16))
# print(digital_root(942))

# Best
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))
