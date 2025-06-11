from typing import List 


def binary_search(nums: List[int], target: int) -> int:
    def inner(i, j):
        if i > j: return -1

        middle = (i + j) // 2
        val = nums[middle]

        if val == target: return middle
        elif val < target: i = middle + 1
        else: j = middle - 1

        return inner(i, j)
    return inner(0, len(nums))


if __name__ == "__main__":
    print(binary_search(nums = [-1,0,3,5,9,12], target = 9))
    print(binary_search(nums = [-1,0,3,5,9,12], target = 2))