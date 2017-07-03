# URL: https://www.codewars.com/kata/take-a-ten-minute-walk/train/python


def isValidWalk(walk):
    direction_value_dict = {'n': 1, 's': -1, 'e': 1, 'w': -1}
    walk_range = 0
    for direction in walk:
        walk_range += direction_value_dict[direction]
    if walk_range == 0 and len(walk) == 10:
        return True
    return False
