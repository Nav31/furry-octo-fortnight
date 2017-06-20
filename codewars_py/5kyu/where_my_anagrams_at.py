# URL: https://www.codewars.com/kata/where-my-anagrams-at/train/python


def is_anagram(word_a, word_b):
    return "".join(sorted(word_a)) == "".join(sorted(word_b))


def anagrams(word, words):
    return [some_word for some_word in words if is_anagram(word, some_word)]


# Best
def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]