def tower_builder(n_floors):
    return_list = []
    base = "*"
    max_asterisk_count = (n_floors*2)-1
    previous_floor_sum = 1
    counter = 1
    for i in range(1, n_floors+1):
        spaces = max_asterisk_count - previous_floor_sum
        previous_floor_sum += 2
        temp_string = " " * (spaces//2)
        temp_string += base * counter
        counter += 2
        temp_string += " " * (spaces//2)
        return_list.append(temp_string)
    return return_list
print tower_builder(6)

# Best
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]