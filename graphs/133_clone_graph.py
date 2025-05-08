from typing import Optional, List

class Node:
    def __init__(self, val: int = None, neighbors:Optional[List['Node']] = None):
        self.val = val
        self.neighbors = neighbors or []
    
    def __str__(self):
        return str(self.val)

def clone_graph(node: Optional['Node']) -> Optional['Node']:
    if node: 
        clone_nodes = {}
        queue = [node]

        while queue:
            temp = queue.pop(0)
            clone_nodes[temp.val] = Node(temp.val)

            for neighbor in temp.neighbors:
                if neighbor.val not in clone_nodes:
                    queue.append(neighbor)

        queue = [node]
        visited = set([node.val])

        while queue:
            temp = queue.pop(0)
            clone_node = clone_nodes[temp.val]

            for neighbor in temp.neighbors:
                clone_node.neighbors.append(clone_nodes[neighbor.val])
                if neighbor.val not in visited:
                    visited.add(neighbor.val)
                    queue.append(neighbor)
        
        for node in clone_nodes.values():
            return node


if __name__ == "__main__":
    one, two, three, four = Node(1), Node(2), Node(3), Node(4)
    
    one.neighbors = [two, four]
    two.neighbors = [one, three]
    three.neighbors = [two, four]
    four.neighbors = [one, three]

    clone_graph(one)