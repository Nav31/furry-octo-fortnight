def prefill(amount, value):
    if amount == 0:
        return []
    elif type(amount) is not int and not amount.isdigit():
        return  TypeError(amount + " is invalid")
    else:
        return_list = []
        for i in range(int(amount)):
            if value:
                return_list.append(value)
            else:
                return_list + None
        return return_list

print prefill("xyz", 1)

