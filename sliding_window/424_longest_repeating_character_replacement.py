from collections import defaultdict
def character_replacement(s: str, k: int) -> int:
    counter = {}
    i = 0
    maxlen = 0

    for j in range(len(s)):
        char = s[j]
        counter[char] = 1 + counter.get(char, 0)

        while ((j - i + 1) - max(counter.values())) > k:

            counter[s[i]] -= 1
            i += 1

        maxlen = max(maxlen, j - i + 1)
    
    return maxlen

if __name__ == "__main__":
    print(character_replacement(k=4, s="KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"))
    print(character_replacement("aabba", k=1))
    print(character_replacement(s="baaab", k=2))
    # print(character_replacement(k=7, s="EOEMQLLQTRQDDCOERARHGAAARRBKCCMFTDAQOLOKARBIJBISTGNKBQGKKTALSQNFSABASNOPBMMGDIOETPTDICRBOMBAAHINTFLH"))