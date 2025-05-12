from typing import List 
from collections import deque


def oranges_rotting(grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    queue = deque([])
    minutes = 0
    fresh = 0
    
    def is_fresh(x, y):
        nonlocal fresh

        if x >=0 and x < ROWS and y >= 0 and y < COLS and grid[x][y] == 1:
            grid[x][y] = 2
            fresh -= 1
            queue.append((x, y))
            return True
    
    for row in range(ROWS):
        for col in range(COLS):   
            if grid[row][col] == 2:    
                queue.append((row, col))
            elif grid[row][col] == 1:
                fresh += 1
                
    while queue:
        flag = False

        for i in range(len(queue)):
            x, y = queue.popleft()
        
            if is_fresh(x + 1, y): flag = True
            if is_fresh(x - 1, y): flag = True
            if is_fresh(x, y + 1): flag = True
            if is_fresh(x, y - 1): flag = True

        if flag:
            minutes += 1

    return -1 if fresh else minutes
        

if __name__ == "__main__":
    print(oranges_rotting(grid=[[2,1,1],[1,1,0],[0,1,1]]))
    print(oranges_rotting(grid=[[2,1,1],[1,1,1],[0,1,2]]))
    print(oranges_rotting(grid=[[2,1,1],[0,1,1],[1,0,1]]))