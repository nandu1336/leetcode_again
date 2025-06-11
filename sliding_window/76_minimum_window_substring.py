##### INCOMPLETE ##########
import math

def min_window(s: str, t: str) -> str:
    if len(s) < len(t): return ""
    
    res, reslen = None, math.inf
    t_counter = {}
    s_counter = {}

    for i in range(len(t)):
        s_counter[s[i]] = 1 + s_counter.get(s[i], 0)
        t_counter[t[i]] = 1 + t_counter.get(t[i], 0)
    
    have, need = 0, len(t_counter)
    
    for char in t_counter.keys():
        have += 1 if char in s_counter and s_counter[char] >= t_counter[char] else 0

    start = 0
    for end in range(len(t),len(s) + 1):
        while have == need:
            if end - start - 1 < reslen:
                res = (start, end)
                reslen = end - start - 1

            char = s[start]
            s_counter[char] -= 1
            start += 1 

            if char in t_counter and s_counter[char] < t_counter[char]: have -= 1
        
        if end == len(s): break
        char = s[end]
        s_counter[char] = 1 + s_counter.get(char, 0)

        if char in t_counter and s_counter[char] == t_counter[char]: have += 1
        
        
    if res is not None:
        l, r = res
        return s[l: r]
    
    return ""

    


if __name__ == "__main__":
    print(min_window(s="ADOBECODEBANC",t="ABC"))
    print(min_window(s="a", t="aa"))
    print(min_window(s="a", t="a"))
    print(min_window(s="cabwefgewcwaefgcf", t="cae"))
    print(min_window(s="ab", t="a"))