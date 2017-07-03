# URL: https://www.codewars.com/kata/palindrome-chain-length

def sum_dict_pair(ints, s):
  memo = {}
  for num in ints:
    sub = s - num
    if sub in memo:
        return [sub, num]
    else:
      memo[num] = 0

l5= [10, 5, 2, 3, 7, 5]
print sum_dict_pair(l5, 10)