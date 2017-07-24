# Tic-Tac-Toe Checker
# URL: https://www.codewars.com/kata/tic-tac-toe-checker/train/python


def isSolved(board):
    isSolved, game_complete = -1, False
    # iterate horizontally to see if all three are the same
    for row in board:
        if row[0] == row[1] and row[1] == row[2]:
            return 1
    # iterate vertically to see if all three are the same
    for idx, val in enumerate(board):
        if board[0][idx] == board[1][idx] and board[1][idx] == board[2][idx]:
            return 1
    # diagonally to the left check
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return 1 

    # iterate diagonally to the right
    # print(board[0][2], board[1][1], board[1][2])
    if board[0][2] == board[1][1] and board[1][1] == board[1][2]:
        return 1
    
    # check for empty spaces
    for row in board:
        if row[0] == 0 or row[1] == 0 or row[2] == 0:
            isSolved = -1
    
    return isSolved if isSolved == -1 else 0

print isSolved([[0,0,1], [0,1,2], [2,1,0]])