from typing import List 


def is_valid_sudoku_board(board: List[List[int]]) -> bool:
    
    n = len(board)
    
    for row in range(n):
        for column in range(n):

            val = board[row][column]
            if val == 0: continue

            for i in range(n):

                if i != column and board[row][i] == val: return False
                if i != row and board[i][column] == val: return False 
    
    return True

from collections import defaultdict

def is_valid_sudoku_board_2(board: List[List[int]]) -> bool:

    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)
    n = len(board)

    for i in range(n):
        for j in range(n):

            val = board[i][j]
            if val == 0: continue

            if val in rows[i] or val in cols[j] or val in squares[(i//3, j//3)]: return False 

        rows[i].add(val)
        cols[j].add(val)
        squares[(i//3, j//3)].add(val)

    return True 

if __name__ == "__main__":
    board = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]
    print(is_valid_sudoku_board_2(board))