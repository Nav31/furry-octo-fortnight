# URL: https://www.codewars.com/kata/playing-with-digits


def dig_pow(n, p):
    split_num = list(str(n))
    num_raised_pow = 0
    for i, num in enumerate(split_num):
        num_raised_pow += int(num) ** (p+i)
    for i in range(1, n+3000):
        if num_raised_pow / i == n:
            return i
    return -1

# Best
def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1