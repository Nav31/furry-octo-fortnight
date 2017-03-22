def comp(array1, array2):
    if array2 == None: return False
    array1 = sorted(array1)
    array2 = sorted(array2)
    for idx, num in enumerate(array1):
        if num*num != array2[idx]:
            return False
    return True

def comp(a1, a2):
    return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)