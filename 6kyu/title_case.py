def title_case(title, *args):
    title = title.lower()
    title = title[0][0].upper() + title[0][1:] + title[1:]
    return_word = ""
    args =  args
    for word in title.split():
        # print word
        if word not in args:
            return_word += word[0].upper() + word[1:] + " "
        else:
            return_word += word + " "
    return return_word

print title_case('a clash of KINGS', 'a an the of')