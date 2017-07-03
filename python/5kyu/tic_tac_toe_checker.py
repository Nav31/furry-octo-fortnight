# Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an X, or 2 if it is an O, like so:
def isSolved(board):
    # return -1 if the board is not solved yet, 1 if X won, 2 if O won, or 0 if it's a draw

    empty_spots = 0
    # for horizontal win and check for 0's aka empty spots
    for array in board:
        if array[0] == array[1] and array[1] == array[2] and array[0] != 0:
            return array[0]
        if 0 in array:
            empty_spots += 1

    # check for vertical win
    for idx, array in enumerate(board):
        if board[0][idx] == board[1][idx] and board[1][idx] == board[2][idx] and board[0][idx] != 0:
            return board[0][idx]

    # check for diagonal-left win
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]

    # check for diagonal-right win
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]

    if empty_spots > 0:
        return -1
    else:
        return 0

print isSolved([
     [0,0,1],
     [0,1,2],
     [2,1,0]
])