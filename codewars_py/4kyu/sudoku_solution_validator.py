# URL: https://www.codewars.com/kata/sudoku-solution-validator

def validSolution(board):
    """A function that checks to see if a sudoku solution is valid"""

    def is_fourty_five(arr):
        """Takes in an list and checks if it is equal to 45"""
        return sum(arr) == 45

    # Do a horizontal check of all lists
    for sub_list in board:
        if not is_fourty_five(sub_list):
            return False

    # Do a vertical check of all the columns
    for idx, sub_list in enumerate(board):
        vertical_arr = []
        for sub_idx, sub_val in enumerate(sub_list):
            vertical_arr.append(board[sub_idx][idx])
        if not is_fourty_five(vertical_arr):
            return False

    # Do a 3x3 grid check
    for i in range(0, len(board), 3):
        for j in range(0, 3):
            print board[i][j]
    return True

print validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                     [6, 7, 2, 1, 9, 5, 3, 4, 8],
                     [1, 9, 8, 3, 4, 2, 5, 6, 7],
                     [8, 5, 9, 7, 6, 1, 4, 2, 3],
                     [4, 2, 6, 8, 5, 3, 7, 9, 1],
                     [7, 1, 3, 9, 2, 4, 8, 5, 6],
                     [9, 6, 1, 5, 3, 7, 2, 8, 4],
                     [2, 8, 7, 4, 1, 9, 6, 3, 5],
                     [3, 4, 5, 2, 8, 6, 1, 7, 9]])

# print validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
#                          [6, 7, 2, 1, 9, 0, 3, 4, 9],
#                          [1, 0, 0, 3, 4, 2, 5, 6, 0],
#                          [8, 5, 9, 7, 6, 1, 0, 2, 0],
#                          [4, 2, 6, 8, 5, 3, 7, 9, 1],
#                          [7, 1, 3, 9, 2, 4, 8, 5, 6],
#                          [9, 0, 1, 5, 3, 7, 2, 1, 4],
#                          [2, 8, 7, 4, 1, 9, 6, 3, 5],
#                          [3, 0, 0, 4, 8, 1, 1, 7, 9]])