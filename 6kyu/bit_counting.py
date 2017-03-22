def countBits(n):
    binaryNum = "{0:010b}".format(n)
    binary_list = (list(str(binaryNum)))
    return len(list(filter(lambda x: x != "0", binary_list)))
print(countBits(1234))

# Best
def countBits(n):
    return bin(n).count("1")