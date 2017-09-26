# https://www.codewars.com/kata/product-of-consecutive-fib-numbers/train/python


def productFib(prod):

    memo = {1:1}

    def fibonacci(n, _cache={}):
        if n in _cache:
            return _cache[n]
        elif n > 1:
            return _cache.setdefault(n, fibonacci(n - 1) + fibonacci(n - 2))
        return n

    for i in range(1, prod+1):
        store = []
        next_fib = fibonacci(i+1)
        store.append(memo[i])   # Gets value from cache a.k.a. memo
        store.append(next_fib)
        memo[i+1] = next_fib    # Assigns value into cache
        current_prod = store[0] * store[1]
        if current_prod == prod:
            store.append(True)
            return store
        if current_prod > prod:
            store.append(False)
            return store

print(productFib(714))
print(productFib(800))
print(productFib(4895))
print(productFib(5895))