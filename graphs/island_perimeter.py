from typing import List 


def island_perimeter(grid: List[List[int]]) -> int: 
    ROWS, COLS = len(grid), len(grid[0])
    perimeter = 0

    def dfs(x, y):
        return x >= 0 and x < ROWS and y >= 0 and y < COLS and grid[x][y] == 1
    
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                
                temp_perimeter = 4

                if dfs(row + 1, col): temp_perimeter -= 1
                if dfs(row - 1, col): temp_perimeter -= 1
                if dfs(row, col + 1): temp_perimeter -= 1
                if dfs(row, col - 1): temp_perimeter -= 1
                
                perimeter += temp_perimeter
    
    return perimeter


if __name__ == "__main__":
    print(island_perimeter(grid=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))