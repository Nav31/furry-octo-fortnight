# https://www.codewars.com/kata/good-vs-evil/train/python

# sample input > goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1')

def goodVsEvil(good, evil):
    #TODO Go get'em boys...

    good_dict = {
        0: 1,
        1: 2,
        2: 3,
        3: 3,
        4: 4,
        5: 10
    }

    evil_dict = {
        0: 1,
        1: 2,
        2: 2,
        3: 2,
        4: 3,
        5: 5,
        6: 10
    }

    good_list, evil_list = good.split(" "), evil.split(" ")
    good_total, evil_total = fight_iter(good_dict, good_list), fight_iter(evil_dict, evil_list)

    str1 = 'Battle Result: Evil eradicates all trace of Good'
    str2 = 'Battle Result: Good triumphs over Evil'
    str3 = 'Battle Result: No victor on this battle field'

    if good_total > evil_total:
        return str2
    elif evil_total > good_total:
        return str1
    else:
        return str3


def fight_iter(side_dict, side_list):
    side_total = 0
    for idx, val in enumerate(side_list):
        side_total += side_dict[idx] * int(val)
    return side_total

print(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1') == 'Battle Result: Evil eradicates all trace of Good')
print(goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0') == 'Battle Result: Good triumphs over Evil')
print(goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0') == 'Battle Result: No victor on this battle field')



