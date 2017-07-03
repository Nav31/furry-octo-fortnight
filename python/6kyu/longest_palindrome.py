def longest_palindrome(s):
    if len(s) == 0: return 0
    longest = 1
    for idx, letter in enumerate(s):
        temp_str = ""
        for next_letters in s[idx:]:
            temp_str += next_letters
            if temp_str == temp_str[::-1] and longest < len(temp_str):
                longest = len(temp_str)
    return longest
print longest_palindrome('a')
print longest_palindrome("aa")
print longest_palindrome("baa")
print longest_palindrome("aab")
print longest_palindrome("abcdefghba")
print longest_palindrome("baablkj12345432133d")