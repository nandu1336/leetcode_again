from typing import List


def surrond_region(board: List[List[str]]):
    ROWS, COLS = len(board), len(board[0])
    excluded = set()
    visited = set()

    def dfs(x, y):
        if (x, y) not in visited and x >= 0 and x < ROWS and y >= 0 and y > COLS and board[x][y] == "O":
            
            visited.add((x, y))
            excluded.add((x, y))

            dfs(x + 1, y)
            dfs(x -1 ,y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            

    for row in range(ROWS):
        for col in range(COLS):
            if (row in (0, ROWS-1) or col in (0, COLS-1)) and board[row][col] == "O":
                dfs(row, col)

    for row in range(1, ROWS):
        for col in range(0, COLS):
            if (row, col) not in excluded:
                board[row][col] = "X"
    
    return board


def surrond_region_2(board: List[List[str]]):
    ROWS, COLS = len(board), len(board[0])
    excluded = set()
    visited = set()
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    def has_O_neighbor(x, y):
        if x >= 0 and x < ROWS and y >= 0 and y < COLS and board[x][y] == "O":
            if (x, y) in excluded or (x in (0, ROWS-1) or y in (0, COLS-1)): return True
            if (x, y) in visited: return False
            visited.add((x, y))
            
            flag = False 

            for dx, dy in directions:
                if has_O_neighbor(x + dx, y + dy): 
                    excluded.add((x + dx, y + dy))
                    flag = True
                    break 
            board[x][y] = "X" if flag else "O"
            return flag 
        return False 
    
    for row in range(ROWS):
        for col in range(COLS):
            if (row in (0, ROWS-1) or col in (0, COLS-1)):
                excluded.add((row, col))
            
            else:
                if board[row][col] == "O":
                    if not has_O_neighbor(row, col): board[row][col] = "X"

    return board
if __name__ == "__main__":
    # print(surrond_region_2([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
    # print(surrond_region_2([["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]))
    print(surrond_region_2([["O","X","O","O","O","X"],["O","O","X","X","X","O"],["X","X","X","X","X","O"],["O","O","O","O","X","X"],["X","X","O","O","X","O"],["O","O","X","X","X","X"]]))