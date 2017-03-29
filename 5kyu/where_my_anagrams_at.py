def anagrams(word, words):
    word = "".join(sorted(list(word)))
    return_list = []
    for someword in words:
        if "".join(sorted(list(someword))) == word:
            return_list.append(someword)
    return return_list

print anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])

# Best
def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]