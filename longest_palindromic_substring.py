def longest_palindromic_substring(string):
    if not string: return 0, ""
    maxlen, res = 1, string[0]
    
    for i in range(len(string)):

        for j in range(len(string)-1, i, -1):
            start = i
            end = j

            while start <= end: 
                if string[start] == string[end]:
                    start += 1
                    end -= 1
                else: 
                    break
            else:
                curlen = j - i + 1
                if maxlen < curlen:
                    maxlen, res = curlen, string[i: j+1]
                break

    return maxlen, res
if __name__ == "__main__":
    print("input: abbacb | output: ", longest_palindromic_substring("abbacb"))
    print("input: a | output: ", longest_palindromic_substring("a"))
    print("input: aabaacaabaa | output: ", longest_palindromic_substring("aabaacaabaa"))
    print("input: acaabcdefhhijklmml | output: ", longest_palindromic_substring("acaabcdefhhijklmml"))
    print("input:  | output: ", longest_palindromic_substring(""))