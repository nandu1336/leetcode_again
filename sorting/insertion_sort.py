def insertion_sort(nums):
    _input  = nums[:]
    n = len(nums)
    for i in range(1, n):
        for j in range(i):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    
    print(f"input: {_input} || output: {nums}")
    


def insertion_sort_traditional(nums):
    _input = nums[:]
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            # print(f"nums: {nums} || key: {key} || j: {j} || nums[j]: {nums[j]} || key < nums[j]: {key < nums[j]}")
            j -= 1
        # print("j: ", j)
        nums[j+1] = key  
        
        
        
    print(f"input: {_input} || output: {nums}")


if __name__ == "__main__":
    insertion_sort_traditional([5, 2, 4, 6, 1, 3])
    insertion_sort_traditional([9, 5, 0, 2, 2, 7, 6, 0, 9, 5])