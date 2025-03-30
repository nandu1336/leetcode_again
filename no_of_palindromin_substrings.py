def no_of_palindromic_substrings(string: str) -> int:
    count = 0
    n = len(string)
    res = []
    def compare_positions(left, right):
        nonlocal string, n, count

        while left > -1 and right < n and string[left] == string[right]:
            res.append(string[left: right + 1])   
            left -= 1 
            right += 1
            count += 1 
        return 

    for i in range(n):
        compare_positions(i, i)
        compare_positions(i, i + 1)

    return count, res 

def no_of_palindromic_substrings2(string: str) -> int:
    n = len(string)
    table = [[0] * n for i in range(n)]
    count = 0

    for i in range(n - 1, -1, -1):
        for j in range(i, n):

            if i == j:
                table[i][j] = 1
            
            elif j == i + 1:
                table[i][j] = string[i] == string[j]
            
            else:
                table[i][j] = string[i] == string[j] and table[i + 1][j - 1]

            if table[i][j]:
                count += 1

    return count 


if __name__ == "__main__":
    for word in ["abaab", "aabaa", "aa"]:
        count, res = no_of_palindromic_substrings(word)
        print(f"input: {word}\ncount: {count}\nproof: {res}")