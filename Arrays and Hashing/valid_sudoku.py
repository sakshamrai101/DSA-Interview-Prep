def isValidSudoku(board):
    # utilise three sets to check if each number is repeating in row, col and in all 3x3 grid.

    # get the dimensions:
    ROWS = len(board)
    COLS = len(board[0])

    # Checking for repeating numbers in the same row. 
    for r in range(ROWS):
        count_1 = set()
        for c in range(COLS):
            if board[r][c] != '.':
                if board[r][c] in count_1:
                    return False
                count_1.add(board[r][c])

    
     # Checking for repeating chars in the same column.
    for c in range(COLS):
        count_2 = set()
        for r in range(ROWS):
            if board[r][c] != '.':
                if board[r][c] in count_2:
                    return False 
                count_2.add(board[r][c])

    
    # Checking for repeating chars in all 3x3 grid
    for i in range(0, ROWS, 3):
        for j in range(0, COLS, 3):
            count_3 = set()
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    if board[r][c] != '.':
                        if board[r][c] in count_3:
                            return False 
                        count_3.add(board[r][c])
    return True
                 


    
            


