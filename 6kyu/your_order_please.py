def order(sentence):
    sentence = sentence.split()
    holder_array = []
    holder_dict = dict()
    for word in sentence:
        temp_word = "".join(sorted((sorted(list(word)))))
        holder_array.append(temp_word)
        holder_dict[temp_word] = word
    newArr = sorted(holder_array)
    for key, value in holder_dict.iteritems():
        idx = [i for i, s in enumerate(newArr) if key in s][0]
        newArr[idx] = value
    return " ".join(newArr)
print order("is2 Thi1s T4est 3a")

# Best
def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))