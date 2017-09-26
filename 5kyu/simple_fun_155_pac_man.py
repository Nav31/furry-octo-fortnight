# https://www.codewars.com/kata/simple-fun-number-155-pac-man/train/python

# NxN => N => Size of the board <INT>
# PM => Position of Pac Man <LIST> [x,y]
# Enemies => position of the enemies on the grid <LIST> either [] OR [[1,2], [3,4], etc...]

def pac_man(N, PM, enemies):

    grid = []

    # Make the grid
    for i in range(N):
        for j in range(N):
            grid.append([i, j])

    # Go through the enemies and remove all the points either with same column or same row as the enemy.
    # Ask: if PM[0] < current_enemy[0] => remove columns with anything current_enemy[0+1, etc...]
    # Do same with Y coordinate
    for enemy in enemies:
        if PM[0] < enemy[0]:
            for i in range(enemy[0], N-1):
                del grid[i]
    # print(grid)


print(pac_man(10,[4, 6],[[0,2], [5,2], [5,5]]))