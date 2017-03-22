def find_outlier(integers):
    even_or_odd_map = {'even': [], 'odd': []}
    for num in integers:
        if num % 2 == 0:
            even_or_odd_map['even'].append(num)
        else:
            even_or_odd_map['odd'].append(num)
    if len(even_or_odd_map['even']) > len(even_or_odd_map['odd']):
        return even_or_odd_map['odd'][0]
    else:
        return even_or_odd_map['even'][0]

print find_outlier([2,6,8,10,3])

# best
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]