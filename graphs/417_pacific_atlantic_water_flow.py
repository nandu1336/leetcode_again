from typing import List 
import math


def pacific_atlantic(heights: List[List[int]]):
    ROWS, COLS = len(heights), len(heights[0])
    pacific, atlantic = set(), set()
    current = set()

    def dfs(x, y, ocean, height=math.inf):
        
        if (x, y) not in current and x >= 0 and x < ROWS and y >= 0 and y < COLS and heights[x][y] <= height:
            if (x, y) in ocean: return True
            
            current.add((x, y))
            
            if dfs(x + 1, y, ocean, heights[x][y]) or\
               dfs(x - 1, y, ocean, heights[x][y]) or\
               dfs(x, y + 1, ocean, heights[x][y]) or\
               dfs(x, y - 1, ocean, heights[x][y]): 
                current.remove((x, y))
                return True
            
            current.remove((x, y))


    for i in range(ROWS):
        pacific.add((i, 0))
        atlantic.add((i, COLS - 1))
    
    for i in range(COLS):
        pacific.add((0, i))
        atlantic.add((ROWS - 1, i))

    for row in range(ROWS):
        for col in range(COLS):

            if dfs(row, col, pacific): 
                pacific.add((row, col))

            if dfs(row, col, atlantic):
                atlantic.add((row, col))

                    
            
    return pacific.intersection(atlantic)

if __name__ == "__main__":
    print(pacific_atlantic(heights=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))