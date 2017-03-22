def iq_test(numbers):
    even_or_odd_map = {"even": [], 'odd': []}
    for index, num in enumerate(numbers.split()):
        if int(num) % 2 == 0:
            even_or_odd_map['even'].append(index+1)
        else:
            even_or_odd_map['odd'].append(index+1)
    if len(even_or_odd_map['even']) > len(even_or_odd_map['odd']):
        return even_or_odd_map['odd'].pop()
    else:
        return even_or_odd_map['even'].pop()

# Best
def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1