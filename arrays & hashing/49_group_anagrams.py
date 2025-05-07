from typing import List 


def group_anagrams(strs: List[str]) -> List[List[str]]:
    tracker = {}

    for str in strs:
        s = "".join(sorted(str))
        if s in tracker:
            tracker[s].append(str)
        else: 
            tracker[s] = [str]

    return tracker.values()        
    

def group_anagrams2(strs: List[str]) -> List[List[str]]: 
    def get_str_code(string):
        alphabet = [0] * 26
        
        for char in string:
            alphabet[ord(char) - 97] += 1
        
        return ".".join([str(alpha) for alpha in alphabet])

    tracker = {}

    for string in strs:
        code = get_str_code(string)
        if code in tracker: 
            tracker[code].append(string)
        else:
            tracker[code] = [string]
    
    return list(tracker.values())

if __name__ == "__main__":
    # print(group_anagrams2(strs=["eat","tea","tan","ate","nat","bat"]))
    print(group_anagrams2(strs=["bdddddddddd","bbbbbbbbbbc"]))