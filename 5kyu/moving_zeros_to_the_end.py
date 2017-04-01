def move_zeros(array):
    # Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
    for idx, char in enumerate(array):
        # print str(char), str(char) == str('False')
        if char == 0:
            print array, idx
            array.remove(array[idx])
            array.append(0)
            print array
    return array

# print move_zeros([1,2,0,1,0,1,0,3,0,1]) # [ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ]
print move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9])
# ["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0]
# ['a', 'b', None, 'c', 'd', 1, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# ['a', 'b', None, 'c', 'd', 1, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
