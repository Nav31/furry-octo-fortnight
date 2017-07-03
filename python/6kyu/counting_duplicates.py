def duplicate_count(text):
    text = text.lower()
    return_count = 0
    duplicate_map = dict()
    for char in text:
        if char in duplicate_map:
            duplicate_map[char] += 1
        else:
            duplicate_map[char] = 1
    for key, value in duplicate_map.iteritems():
        if value > 1:
            return_count += 1
    return return_count

# print duplicate_count("abcdea")

# best
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])