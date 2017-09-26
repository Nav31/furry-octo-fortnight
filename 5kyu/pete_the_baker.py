# https://www.codewars.com/kata/pete-the-baker/train/python

"""
# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
"""

def cakes(recipe, available):
    results = []
    for key, val in recipe.items():
        if key in available:
            results.append(available[key] / val)
        else:
            return 0
    return min(results)

print(cakes(
    {
        "flour": 500,
        "sugar": 200, "eggs": 1
    },
    {
        "flour": 1200,
        "sugar": 1200,
        "eggs": 5,
        "milk": 200
    }
))