def move_zeros(array):
    # Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
    for idx, char in enumerate(array):
        if char == 0:
            print array, idx
            array.remove(array[idx])
            array.append(0)
            print array
    return array

print move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9])
