def find_it(seq):
    occuranceFreqMap = dict()
    for num in seq:
        if(num in occuranceFreqMap):
            occuranceFreqMap[num] += 1
        else:
            occuranceFreqMap[num] = 1
    for key, val in occuranceFreqMap.items():
        if(val % 2 != 0):
            return int(key)

# Best
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i