# URL: https://www.codewars.com/kata/moving-zeros-to-the-end/train/python


def move_zeros(array):
    for i, char in enumerate(array):
        if int(float(char)) == 0:
            del array[i]
            array.append(char)
    return array

print move_zeros(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))