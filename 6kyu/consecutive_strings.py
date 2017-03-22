def longest_consec(arr, k):
    longest_string = ""
    temp_string = ""
    if k <= 0: return ""
    if k > len(arr): return ""
    for num in range(len(arr)+1):
        for word in arr[num: num + k]:
            temp_string += word
        if len(temp_string) > len(longest_string):
            longest_string = temp_string
        temp_string = ""
    return longest_string

# print longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)
print longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2)
# print len("wlwsasphmxxowiaxujylentrklctozmymu"), len("owiaxujylentrklctozmymuwpgozvxxiu")

# Best
def longest_consec(strarr, k):
    result = ""
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            
    return result