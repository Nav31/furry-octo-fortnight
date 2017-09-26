# https://www.codewars.com/kata/directions-reduction/train/python


def dirReduc(arr):
    if len(arr) < 1:
        return arr
    opposite_dir = {"NORTH": "SOUTH", "EAST": "WEST", "SOUTH": "NORTH", "WEST": "EAST"}
    direction_stack = [arr[0]]
    for direction in arr[1:]:
        if len(direction_stack) > 0:
            if opposite_dir[direction] == direction_stack[-1]:
                direction_stack.pop()
            else:
                direction_stack.append(direction)
        else:
            direction_stack.append(direction)
    return direction_stack

print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))
print(["WEST"])
