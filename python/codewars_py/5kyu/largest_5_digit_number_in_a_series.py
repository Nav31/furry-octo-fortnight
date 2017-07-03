# URL: https://www.codewars.com/kata/largest-5-digit-number-in-a-series


def solution(digits):
    highest = 0
    for idx, num in enumerate(digits[:-4]):
        current_num = int(digits[idx] + digits[idx+1] + digits[idx+2] + digits[idx+3] + digits[idx+4])
        if current_num > highest:
            highest = current_num
    return highest

# Best
def solution(dd):
    return max(int(dd[i:i+5]) for i in range(len(dd) - 4))