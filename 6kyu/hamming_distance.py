def hamming(a,b):
    # hamming("I like turtles","I like turkeys")  //returns 3
    diff_count = 0
    for idx, char in enumerate(b):
        if a[idx] != char:
            diff_count += 1
    return diff_count