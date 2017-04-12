def mineLocation(field):
    for idx, array in enumerate(field):
        for sub_idx, element in enumerate(array):
            if element == 1:
                return [idx, sub_idx]