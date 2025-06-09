from typing import List 


def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    numlen = len(nums)

    def backtracking(combo, i):
        res.append(combo[:])

        for j in range(i, numlen):
            if j > i and nums[j-1] == nums[j]: continue

            combo.append(nums[j])
            backtracking(combo, j+1)
            combo.pop()

    backtracking([], 0)
    return res


if __name__ == "__main__":
    print(subsets_with_dup([1, 2, 2]))