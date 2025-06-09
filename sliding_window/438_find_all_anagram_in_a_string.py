from typing import List 

a = ord('a')

def get_counter(string):
    counter = [0] * 26
    
    for char in string:
        index = ord(char) - a
        counter[index] += 1
    
    return counter

def find_anagrams(s: str, p: str) -> List[int]: 
    if len(p) > len(s): return []
    res = []
    start, end, matches = 0, len(p), 0 
    p_counter = get_counter(p)
    s_counter = get_counter(s[start: end])
    

    for i in range(26): 
        matches += 1 if p_counter[i] == s_counter[i] else 0

    while end < len(s):
        if matches == 26: 
            res.append(start)

        index = ord(s[start]) - a
        s_counter[index] -= 1

        if s_counter[index] == p_counter[index]: matches += 1
        if s_counter[index] + 1 == p_counter[index]: matches -= 1

        index = ord(s[end]) - a
        s_counter[index] += 1

        if s_counter[index] == p_counter[index]: matches += 1
        if s_counter[index] - 1 == p_counter[index]: matches -= 1
        
        start, end = start + 1, end + 1
    
    if matches == 26: res.append(start)
    return res


if __name__ == "__main__":
    # print(find_anagrams(s="cbaebabacd", p="abc"))
    print(find_anagrams("abab", "ab"))

