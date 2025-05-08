from typing import List 


def max_area_of_island(grid: List[List[int]]) -> int: 
    ROWS, COLS = len(grid), len(grid[0])
    max_area = 0

    def dfs(x, y, area=0):
        nonlocal ROWS, COLS
        
        if x >= 0 and x < ROWS and y >= 0 and y < COLS and grid[x][y] == 1:
            grid[x][y] = 0
            area += 1

            area = dfs(x + 1, y, area)
            area = dfs(x - 1, y, area)
            area = dfs(x, y + 1, area)
            area = dfs(x, y - 1, area)
    
        return area
    
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                area = dfs(row, col)
                max_area = area if area > max_area else max_area
    
    return max_area


if __name__ == "__main__":
    print("main called")
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(max_area_of_island(grid))
