from typing import List 


def daily_temperatures(temperatures: List[int]) -> List[int]:
    temperatures=[73,74,75,71,69,72,76,73]
    n = len(temperatures)
    stack = []
    res = [0] * n 

    for i, temp in enumerate(temperatures):
        dist = 1
        while stack and stack[-1] < temp:
            res[i - dist] = dist
            stack.pop()            
            dist += 1

        stack.append(temp)

    return res


if __name__ == "__main__":
    print(daily_temperatures(temperatures=[73,74,75,71,69,72,76,73]))