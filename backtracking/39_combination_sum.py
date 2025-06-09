from typing import List 


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    res = []
    numlen = len(candidates)
    
    def inner(temp, i, _sum):
        if _sum == target:
            res.append(temp[:])
            return
        
        if _sum > target: 
            return True
        
        for j in range(i, numlen):
            temp.append(candidates[j])
            if inner(temp, j, _sum+candidates[j]): 
                temp.pop(-1)
                break
            temp.pop(-1)

    for index, num in enumerate(candidates):
        inner([num], index, num)
    
    return list(res)


if __name__ == "__main__":
    print(combination_sum([2, 3, 6, 7], target=6))