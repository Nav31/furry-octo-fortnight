def array_diff(a,b):
    ans = []
    for num in a:
        if b.count(num) == 0:
            ans.append(num)
    return ans
    
# Best Solution
def array_diff(a, b):
    return [x for x in a if x not in b]