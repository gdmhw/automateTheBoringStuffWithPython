grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


# print grid[0][0] -> grid[8][0] grid[i] -> [i]
# then grid[0][1] -> grid[1][1] -> grid[2][1]....

# pass the end keyword argument to print() to avoid a newline after each print()


for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end='')
    print('')

