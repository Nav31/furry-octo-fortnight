# Next bigger number with the same digits
# URL: https://www.codewars.com/kata/next-bigger-number-with-the-same-digits


def next_bigger(numb):

    numb_list = list(str(numb))
    max_num = int(''.join(sorted(numb_list, reverse=True)))

    if numb == max_num or len(numb_list) == 1:
        return -1

    for i in range(numb, max_num+1):
        numb += 1
        if int("".join(sorted(list(str(numb)), reverse=True))) == max_num:
            return numb

# print(next_bigger(12))
# print(next_bigger(513))
# print(next_bigger(414))
print(next_bigger(2017))
# print(next_bigger(123456789))

