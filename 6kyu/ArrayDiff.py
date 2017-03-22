# https://www.codewars.com/kata/523f5d21c841566fde000009/solutions/python
def array_diff(a,b):
    ans = []
    for num in a:
        if b.count(num) == 0:
            ans.append(num)
    return ans
    
# Best Solution
def array_diff(a, b):
    return [x for x in a if x not in b]