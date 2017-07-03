def get_sum(a,b):
    if(a == b):
        return a
    else:
        sumVal = 0
        larger = a
        smaller = b
        if(a>b):
            larger = a
            smaller = b
        else:
            larger = b
            smaller = a
        for num in range(smaller, larger+1):
            sumVal += num
        return sumVal

print(get_sum(0,-1))

# best
def get_sum(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))

# Good
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))