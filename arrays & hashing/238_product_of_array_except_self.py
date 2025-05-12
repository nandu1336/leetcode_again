from typing import List


def product_except_self(nums: List[int]) -> int: 
    n = len(nums)
    lp, rp = 1, 1
    i, j = 1, n - 2
    res = [1]* n

    while i < n:
        temp = lp * nums[i - 1]
        res[i] *= temp 
        lp = temp

        temp = rp * nums[j + 1]
        res[j] *= temp
        rp = temp

        i += 1
        j -= 1

    
    return res


if __name__ == "__main__":
    print(product_except_self(nums=[1,2,3,4]))