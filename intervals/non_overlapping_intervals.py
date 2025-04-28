from typing import List 


def merge(first_interval: List[int], second_interval: List[int]) -> List[int]:
        return [min(first_interval[0], second_interval[0]), max(first_interval[1], second_interval[1])]

def get_larger_interval(): 
    pass 

def has_overalap(first_interval: List[int], second_interval: List[int]) -> bool:
    el, eh = first_interval
    nl, nh = second_interval
    
    return (nl < el and nh > el) or (nl > el and nl < eh)

def non_overlapping_intervals(intervals: List[int]) -> int:
    intervals.sort(key=lambda item: item[0])

    prev = intervals[0]
    for index in range(1, len(intervals)):
        cur = intervals[index]

        if has_overalap(prev, cur):
            get_larger_interval(prev, cur) 
            pass 


if __name__ == "__main__":
    non_overlapping_intervals(intervals=[[1,2],[2,3],[3,4],[1,3]])