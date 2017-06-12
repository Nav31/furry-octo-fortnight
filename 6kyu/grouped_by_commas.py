def group_by_commas(n):
    n = str(n)
    counter = len(n)-1
    # return_string = ""
    return_string = ""
    while counter > 0:
        # print n[counter]
        print counter
            return_string += ","
        else:
            return_string += n[counter] + n[counter-1] + n[counter-2]
        counter -= 2
    return return_string
print group_by_commas(35235235)

# print group_by_commas(1000000)
