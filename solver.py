import pprint

def solve(board):
    find = findEmpty(board)
    if find:
        row, col = find
    else:
        return True

    for i in range(1, 10):
        if valid(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True
            
            board[row][col] = 0
    return False

def valid(board, pos, num):
    # check row
    for i in range(0, len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    # check column
    for i in range(0, len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    # check each 3x3 cell
    cell_x = pos[1] // 3
    cell_y = pos[0] // 3

    for i in range(3 * (cell_y), 3 + (3*cell_y)):
        for j in range(3 * (cell_x), 3 + (3*cell_x)):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    return True

# finds empty square on the board
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return


# utility function to print the board
def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0:
               print(" | ",end="") 
            
            if j == 0:
                print(board[i][j])
            
            else:
                print(str(board[i][j]) + " ", end = "")

b1 = [
    [5, 1, 7, 6, 0, 0, 0, 3, 4],
    [2, 8, 9, 0, 0, 4, 0, 0, 0],
    [3, 4, 6, 2, 0, 5, 0, 9, 0],
    [6, 0, 2, 0, 0, 0, 0, 1, 0],
    [0, 3, 8, 0, 0, 6, 0, 4, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 7, 8],
    [7, 0, 3, 4, 0, 0, 5, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

b2 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

b3 = [
    [0, 0, 0, 4, 9, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 7, 6, 0],
    [0, 8, 0, 0, 0, 7, 2, 0, 0],
    [0, 9, 0, 0, 8, 0, 0, 5, 0],
    [4, 5, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 6, 0, 0, 0, 1, 0, 3],
    [7, 0, 0, 0, 3, 0, 0, 0, 0],
    [0, 0, 8, 9, 0, 0, 0, 0, 0]
]


pp = pprint.PrettyPrinter(width=41, compact=True)

solve(b1)
pp.pprint(b1)

print()

solve(b2)
pp.pprint(b2)

print()

solve(b3)
pp.pprint(b3)
