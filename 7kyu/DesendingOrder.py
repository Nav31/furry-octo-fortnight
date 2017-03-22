def Descending_Order(num):
    num = list(str(num))
    num = [int(x) for x in num]
    num = sorted(num, reverse=True)
    num = [str(x) for x in num]
    return int("".join(num))
print(Descending_Order(123456789))

# Best
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))