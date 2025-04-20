from typing import List, Tuple
import heapq


class MaxHeap:
    def __init__(self):
        self.max_heap = []
        
    def push(self, item: Tuple[int, int]) -> None:
        freq, val = item
        freq *= -1
        heapq.heappush(self.max_heap, (freq, val))

    def pop(self) -> int: 
        freq, val = heapq.heappop(self.max_heap)
        return val
    
def top_k_frequent_elements(nums: List[int], k: int) -> List[int]:
    tracker = {}
    
    for num in nums:
        if num in tracker:
            tracker[num] += 1
        else:
            tracker[num] = 1
    
    max_heap = MaxHeap()

    for key, val in tracker.items():
        max_heap.push((val, key))
    
    return [max_heap.pop() for i in range(k)]


def top_k_frequent_elements_2(nums: List[int], k: int) -> List[int]:
    bucket = {}   
    tracker = {}

    for num in nums:
        if num not in tracker: 
            tracker[num] = 1
        else:
            tracker[num] += 1
    
    for key, value in tracker.items():
        if value in bucket:
            bucket[value].append(key)
        else:
            bucket[value] = [key]

    res = []
    for i in range(5, -1, -1):
        if len(bucket[i]) > 0:
            for num in bucket[i]:
                if len(res) == k: return res
                res.append(num)
    return res

if __name__ == "__main__":
    # print(top_k_frequent_elements_2(nums = [1,1,1,2,2,3], k = 2))
    # print(top_k_frequent_elements_2(nums=[1], k=1))
    nums = [5,1,-1,-8,-7,8,-5,0,1,10,8,0,-4,3,-1,-1,4,-5,4,-3,0,2,2,2,4,-2,-4,8,-7,-7,2,-8,0,-8,10,8,-8,-2,-9,4,-7,6,6,-1,4,2,8,-3,5,-9,-3,6,-8,-5,5,10,2,-5,-1,-5,1,-3,7,0,8,-2,-3,-1,-5,4,7,-9,0,2,10,4,4,-4,-1,-1,6,-8,-9,-1,9,-9,3,5,1,6,-1,-2,4,2,4,-6,4,4,5,-5]
    k = 7

    print(top_k_frequent_elements_2(nums, k))