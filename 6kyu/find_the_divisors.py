def divisors(integer):
    divisors_list = []
    for num in range(2, integer):
        if integer % num == 0:
            divisors_list.append(num)
    if len(divisors_list) == 0:
        return "%d is prime" % (integer)
    else: 
        return divisors_list

#  best
def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l