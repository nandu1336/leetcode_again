from typing import List 


def combination_sum_2(candidates: List[int], target: int) -> List[List[int]]: 
    candidates.sort()
    res = []
    tracker = set()

    numlen = len(candidates)

    def inner(index, total, combo):
        if total == target:
            combo_as_string = str(combo)
            if combo_as_string not in tracker:
                tracker.add(combo_as_string)
                res.append(combo[:])
        
        if total > target: return 

        for j in range(index, numlen):
            combo.append(candidates[j])
            inner(j+1, total + candidates[j], combo)
            combo.pop()

    inner(0, 0, [])
    return res


if __name__ == "__main__":
    print(combination_sum_2(candidates = [10,1,2,7,6,1,5], target = 8))