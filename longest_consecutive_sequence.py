from typing import List 
import math 
import heapq


class Heap:
    def __init__(self):
        self.heap = []

    def push(self, num: int) -> None:
        heapq.heappush(self.heap, num)

    def pop(self) -> int: 
        return heapq.heappop(self.heap)
    
    def __len__(self):
        return len(self.heap)
    

def longest_consecutive_sequence(nums: List[int]) -> int:
    tracker = set()
    min_heap = Heap()
    
    for num in nums:
        if num not in tracker: 
            min_heap.push(num)
        tracker.add(num)

    current_max, temp = 0, 0
    last = None

    while len(min_heap):
        val = min_heap.pop()
        
        if last is None or val == last + 1:
            temp += 1
        
        else :
            current_max = current_max if current_max > temp else temp
            temp = 1

        last = val

    return current_max if current_max > temp else temp

if __name__ == "__main__":
    # print(longest_consecutive_sequence([100,4,200,1,3,2]))
    # print(longest_consecutive_sequence([0,3,7,2,5,8,4,6,0,1]))
    # print(longest_consecutive_sequence([9,1,4,7,3,-1,0,5,8,-1,6]))
    print(longest_consecutive_sequence([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]))