def find_missing(sequence):
    if sequence[:-1][0] < 0:
        offset = -1
        negative_progression = True
    else:
        offset = 1
    # determine step size
    if len(sequence) > 2:
        step = sequence[-1:][0] - sequence[-2:][0]
    else:
        step = sequence[1:][0] - sequence[:1]
    # This gives the full range of numbers
    full_range = [num for num in range(sequence[:1][0],int(sequence[-1:][0]) + offset, step)] # range from 1 to last number in array
    # Turn list into set
    set_full_range = set(full_range)
    # print full_range
    for num in set_full_range:
        print(num)
        if num not in sequence:
            return num