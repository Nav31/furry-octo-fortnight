# url: https://www.codewars.com/kata/multiples-of-3-and-5/python

def solution(number):
    num_holder = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            num_holder.append(i)
    return sum(num_holder)

# Best
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

