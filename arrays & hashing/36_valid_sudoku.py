from typing import List 


def is_valid_sudoku(board: List[List[int]]): 
    ROWS, COLS = len(board), len(board[0])

    cols_set = {}
    square_set = {}

    for r in range(ROWS):
        rows_set = set()

        for c in range(COLS):
            value = board[r][c]

            if value != ".":
                if value in rows_set: return False 
                rows_set.add(value)

                if c in cols_set:
                    if value in cols_set[c]: return False 
                    cols_set[c].add(value)
                else: 
                    cols_set[c] = set([value]) 

                
                square = (r//3, c//3)
                if square in square_set:
                    if value in square_set[square]: return False
                    square_set[square].add(value)
                
                else:
                    square_set[square] = set([value])

        return True

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    
    print(is_valid_sudoku(board))