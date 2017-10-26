def scramble(s1, s2):
    if len(s2) > len(s1):
        return False
    char_map = {}
    build_str = ""
    for char in s1:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1
    for char in s2:
        if char not in char_map:
            return False
        else:
            if char_map[char] <= 0:
                return False
            else:
                build_str += char
                char_map[char] -= 1
    return True


# __Best__

def scramble(s1,s2):
    for char in set(s2):
        if s1.count(char) < s2.count(char):
            return False
    return True

