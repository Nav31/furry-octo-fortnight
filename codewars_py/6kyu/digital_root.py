# URL: https://www.codewars.com/kata/sum-of-digits-slash-digital-root/python

def digital_root(n):
    str_num = str(n)
    if len(str_num) == 1:
        return n
    else:
        count = 0
        num_list = [int(d) for d in str(n)]
        for num in num_list:
          count += num
        return digital_root(count)

# Best
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))