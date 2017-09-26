# https://www.codewars.com/kata/double-cola/train/python


def whoIsNext(names, r):
    count = 1
    while count < r:
        name = names.pop(0)
        names.append(name)
        names.append(name)
        count += 1
    return names[0]

print(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52))