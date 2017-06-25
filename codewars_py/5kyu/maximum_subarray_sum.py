# URL: https://www.codewars.com/kata/maximum-subarray-sum/train/python


def maxSequence(arr):
    highest_sum = 0
    return_list, all_neg = [], True
    for idx, val in enumerate(arr):
        for sub_idx, sub_val in enumerate(arr):
            current_list_sum = sum(arr[idx:sub_idx+1])
            if sub_val > 0:
                all_neg = False
            if current_list_sum > highest_sum:
                highest_sum = current_list_sum
    return 0 if all_neg else highest_sum

# Clever
def maxSequence(arr):
  lowest = ans = total = 0
  for i in arr:
    total += i
    lowest = min(lowest, total)
    ans = max(ans, total - lowest)
  return ans

