from typing import List


def merge(first_interval: List[int], second_interval: List[int]) -> List[int]:
        return [min(first_interval[0], second_interval[0]), max(first_interval[1], second_interval[1])]

def has_overalap(first_interval: List[int], second_interval: List[int]) -> bool:
    el, eh = first_interval
    nl, nh = second_interval
    
    return (nl <= el and nh >= el) or (nl >= el and nl <= eh)

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    res = [] 
    intervals.sort()    
    prev = intervals[0]
    
    for index in range(1, len(intervals)):
        cur = intervals[index]
        
        if has_overalap(prev, cur):
            prev = merge(prev, cur)

        else:
            res.append(prev)
            prev = cur
    
    if prev:
        res.append(prev)

    return res


if __name__ == "__main__": 
    print(merge_intervals(intervals=[[1,3],[2,6],[8,10],[15,18]]))
    print(merge_intervals(intervals=[[1, 3]]))
    print(merge_intervals(intervals=[[2,3],[4,5],[6,7],[8,9],[1,10]]))