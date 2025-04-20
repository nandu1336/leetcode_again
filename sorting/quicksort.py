def paritition(nums, low, high):
    n = len(nums[low: high])
    pivot_value = nums[n-1]
    pivot_index = 0

    for i in range(len(nums[low: high])):
        if nums[i] < pivot_value:
            nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
            pivot_index += 1
    
    nums[pivot_index], nums[n-1] = nums[n-1], nums[pivot_index]
    print(nums, pivot_index)
    return pivot_index


def quicksort(nums, low=None, high=None):
    print(f"nums in quicksort: {nums} || low: {low} || high: {high}")
    if len(nums[low: high]) <= 1: return nums
    low = low or 0 
    high = high or len(nums)
    pivot = paritition(nums, low, high)
    
    return quicksort(nums, low, pivot) + quicksort(nums, pivot, high)
     

if __name__ == "__main__":
    print(quicksort([9, 5, 0, 2, 2, 7, 6, 0, 9, 5]))