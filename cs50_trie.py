from typing import List 


class Node:
    def __init__(self, university: str = None):
        self.university = university
        self.keys: List[Node] = [0] * 10

    def as_dict(self):
        def process_node(node):
            if isinstance(node, Node): return node.as_dict()
            return node
            
        return {
            "university": self.university,
            "keys": {index: process_node(node) for index, node in enumerate(self.keys)}
        }

def get_digits(num):
    stack = []
    while num > 0:
        rem = num % 10
        num = num // 10
        stack.append(rem)
    
    while stack:
        yield stack.pop()


def insert(data): 
    # insert
    temp = Node()

    for key, value in data.items():
        root = temp

        for digit in get_digits(key):
            if root.keys[digit] == 0:
                root.keys[digit] = Node()
            
            root = root.keys[digit]

        root.university = value

    # Node flattening
    root = temp 
    return root

def get(university_code, root):
    while root: 
        for digit in get_digits(university_code):
            root = root.keys[digit]
        
        return root.university

if __name__ == "__main__":
    data = {123: "Harvard", 234: "Princeton", 156: "Cornell"}
    root = insert(data)
    import json 
    print(json.dumps(root.as_dict()))

    print(get(123, root))