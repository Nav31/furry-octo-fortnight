# Don't Drink the Water
#url: https://www.codewars.com/kata/dont-drink-the-water/train/python

def separate_liquids (glass):
    density_map = {"H": 1.36, "W": 1.00, "A": .87, "O": .80}
    return_list = []
    if len(glass) == 0:
        return glass
    honey, water, alcohol, oil = [], [], [], []
    for level in glass:
        for char in level:
            if char == 'H':
                honey.append('H')
            if char == 'W':
                water.append('W')
            if char == 'A':
                alcohol.append('A')
            if char == 'O':
                oil.append('O')
    # return_list.append(oil, alcohol, water, honey)
    return_list.append(alcohol)
    return_list.append(water)
    return_list.append(honey)
    return_list = [level for level in return_list if len(level) > 0]
    return return_list

print(separate_liquids([['H', 'H', 'W', 'O'],['W','W','O','W'],['H','H','O','O']]), [['O', 'O', 'O', 'O'],['W','W','W','W'],['H','H','H','H']])