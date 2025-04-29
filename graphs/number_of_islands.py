from typing import List


def number_of_islands(grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    count = 0

    def dfs(i, j):
        nonlocal ROWS, COLS

        if i >= 0 and i < ROWS and j >= 0 and j < COLS and grid[i][j] == "1":   
            grid[i][j] = "X"
            dfs(i + 1, j) 
            dfs(i - 1, j) 
            dfs(i, j + 1) 
            dfs(i, j - 1)

    
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "1":
                count += 1
                dfs(row, col)
    
    return count

if __name__ == "__main__":
    grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    print(number_of_islands(grid))