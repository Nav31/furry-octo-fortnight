# url: https://www.codewars.com/kata/stop-gninnips-my-sdrow/train/python

def spin_words(sentence):
    split_sentence = sentence.split()
    return_list = []
    for word in split_sentence:
        if len(word) >= 5:
            return_list.append(str(word[::-1]))
        else:
            return_list.append(word)
    return " ".join(return_list)

# Best
def spin_words(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)