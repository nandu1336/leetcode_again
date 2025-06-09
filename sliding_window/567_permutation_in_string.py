A = ord('a')

def check_inclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2): return False
    
    start, end, matches = 0, len(s1), 0
    
    s1_counter = [0] * 26
    s2_counter = [0] * 26
    
    for i in range(len(s1)):
        s1_counter[ord(s1[i]) - A] += 1
        s2_counter[ord(s2[i]) - A] += 1

    for i in range(26):
        if s1_counter[i] == s2_counter[i]: 
            matches += 1

    while end < len(s2):
        if matches == 26: return True 
        
        index = ord(s2[start]) - A
        s2_counter[index] -= 1
    
        if s1_counter[index] == s2_counter[index]: matches += 1
        elif s1_counter[index] - s2_counter[index] == 1: matches -= 1
        
        
        index = ord(s2[end]) - A
        s2_counter[index] += 1
    
        if s1_counter[index] == s2_counter[index]: matches += 1
        elif s2_counter[index] - s1_counter[index] == 1: matches -= 1
    
        
        start, end = start + 1, end + 1

    return matches == 26


if __name__ == "__main__":
    print(check_inclusion("ab", "aidbaooo"))
    print(check_inclusion("ab", "eidboaoo"))
    print(check_inclusion("adc", "dcda"))
    print(check_inclusion("abc", "cccccbabbbaaaa"))
    print(check_inclusion("rvwrk", "lznomzggwrvrkxecjaq"))