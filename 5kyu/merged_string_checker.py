def is_merge(str, part1, part2):
    if len(part1) <= 0 or len(part2) <= 0:
        return False
    if part1+part2 == str:
        return str
    else:
        return_string = ""
        diff_len = len(part2) - len(part1)
        for i in range(len(part1)):
            return_string += part1[i:i+1]
            if part2[i:i+1]:
                return_string += part2[i:i+1]
        if diff_len > 0:
            return_string += part2[len(part1):]
        print return_string
        if return_string == str:
            return return_string
    return False

print is_merge("Bananas from Bahamas", "Bahas", 'Bananas from am')