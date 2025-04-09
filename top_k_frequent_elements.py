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



if __name__ == "__main__":
    print(top_k_frequent_elements(nums = [1,1,1,2,2,3], k = 2))