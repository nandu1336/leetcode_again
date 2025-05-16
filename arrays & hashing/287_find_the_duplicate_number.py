from typing import List 


def find_duplicate(nums: List[int]) -> int: 
    p_value, p_index = 0, -1
    n = len(nums)

    for j in range(n):
        start = 0
        for i in range(start, n):
            cur = nums[i]

            if cur == p_value + 1:
                p_value = cur 
                p_index = i
                start = i + 1
            elif cur == p_value and p_index != i: 
                return p_value
            elif cur <= p_value: 
                return cur
            else: 
                start += 1

    return nums[p_index + 1]

if __name__ == "__main__":
    # print(find_duplicate([1, 3, 4, 2, 2]))
    print(find_duplicate([3, 1, 3, 4, 2]))
    # print(find_duplicate([3, 3, 3, 3, 3]))
    # print(find_duplicate([1, 4, 4, 2, 4]))
    # print(find_duplicate([1, 3, 4, 2, 1]))