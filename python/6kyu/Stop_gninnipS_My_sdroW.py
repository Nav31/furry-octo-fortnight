def spin_words(sentence):
    sentence = sentence.split()
    ans = []
    for word in sentence:
        if len(word) >= 5:
            ans.append(word[::-1])
        else:
          ans.append(word)
    return " ".join(ans)
