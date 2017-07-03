# url: https://www.codewars.com/kata/find-the-odd-int/train/python

def find_it(seq):
    count_dict = {}
    for num in seq:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    for key, val in count_dict.items():
        if val % 2 is not 0:
            return key

# Best
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
