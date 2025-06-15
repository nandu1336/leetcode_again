
from tree import Tree
from typing import Optional

def kth_smallest(root: Optional[Tree], k: int) -> int :
    res = []

    def dfs(node): 
        if node: 
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

def kth_smallest_2(root: Optional[Tree], k: int) -> int:        
    ###### INCOMPLETE ######
    stack = [root]
    res = []
    
    while stack:
        node = stack[0]

        while node: 
            stack.append(node.left)
            node = node.left
        stack.pop()
        


if __name__ == "__main__":
    print(kth_smallest(Tree(3, Tree(1, None, Tree(2)), Tree(4)), 1))