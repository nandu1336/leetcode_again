from typing import List, Dict
import json 


class Trie:
    a_ASCII_CODE = ord("a")

    def __init__(self):
        self.is_end = False 
        self.nodes = [0] * 26

    def insert(self, word: str = None, letters: List[str] = None):
        word = word or letters
        root = self
        
        for char in word:
            index = ord(char.lower()) - Trie.a_ASCII_CODE
            
            if root.nodes[index] == 0:
                root.nodes[index] = Trie()

            root = root.nodes[index]
        
        root.is_end = True
        

    def search(self, word):
        word = word.lower()
        root = self

        for char in word:
            
            index = ord(char) - Trie.a_ASCII_CODE
            if root.nodes[index] == 0: return False 
            root = root.nodes[index]

        return root.is_end    
    
    def starts_with(self, word):
        word = word.lower()
        root = self
        
        for char in word:

            index = ord(char) - Trie.a_ASCII_CODE
            if root.nodes[index] == 0: return False 
            root = root.nodes[index]
        
        return True 

    def as_dict(self, root=None):
        root = root or self
        res = {"is_end": root.is_end, "nodes": {}}

        for index, node in enumerate(root.nodes):
            if node != 0:
                res["nodes"][chr(Trie.a_ASCII_CODE + index)] = self.as_dict(node)
        
        return res

class BetterTrie:
    def __init__(self):
        self.is_end: bool = False
        self.nodes: Dict = dict()

    def insert(self, word: str): 
        print(f"inserting: {word}")
        root = self
        for char in word:
            char = char.lower()
            if char not in root.nodes:
                root.nodes[char] = BetterTrie()
            
            root = root.nodes[char]
        root.is_end = True
    
    def search(self, word: str): 
        root = self
        for char in word:
            char = char.lower()
            if char not in root.nodes: return False
            root = root.nodes[char]

        return root.is_end
    
    def starts_with(self, word: str): 
        root = self
        for char in word:
            char = char.lower()
            if char not in root.nodes: return False 
            root = root.nodes[char]
        
        return True
    
    def as_dict(self):
        res = {}

        for key, node in self.nodes.items():
            if node.is_end: return key
            res[key] = node.as_dict()
            
        return res 

    def as_json(self, filepath=None):
        if filepath:
            with open(filepath, 'w') as f:
                json.dump(self.as_dict(), f, indent='\t')
                return 
            
        return json.dumps(self.as_dict())    

if __name__ == "__main__":
    trie: BetterTrie = None
    actions = ["Trie","insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]
    words = [[],["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]
    
    for index, action in enumerate(actions):
        word = words[index]
        
        if action == "Trie":
            trie = BetterTrie()
        
        elif action == "insert":
            trie.insert(word[0])
        
        elif action == "search":
            print(f"{word} in trie: {trie.search(word[0])}")

        elif action == "startsWith":
            print(f"starts with {word} in trie: {trie.starts_with(word[0])}")

    