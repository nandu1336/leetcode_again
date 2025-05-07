def first_non_repeating_charater(string: str) -> int:
    q_index = 0
    res = []
    visited = {}

    for index, char in enumerate(string):
        if char in visited:
            res[visited[char]] = None 
        else:
            visited[char] = q_index
            res.append(index)
            q_index += 1

    for val in res:
        if val is not None: return val
    else:
        return -1


def first_non_repeating_character_2(string: str) -> int: 
    frequency = [0] * 26
    ascii_a = ord('a')

    for char in string:
        frequency[ord(char) - ascii_a] += 1
    
    for index, char in enumerate(string):
        if frequency[char] == 1: return index
    
    return -1

if __name__ == "__main__":
    print(first_non_repeating_charater("leetcode"))
    print(first_non_repeating_charater("aabb"))