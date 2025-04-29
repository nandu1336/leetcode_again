from typing import List

def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    if not intervals: return [new_interval]
    res = []

    def merge(first_interval: List[int], second_interval: List[int]) -> List[int]:
        return [min(first_interval[0], second_interval[0]), max(first_interval[1], second_interval[1])]

    def has_overalap(first_interval: List[int], second_interval: List[int]) -> bool:
        el, eh = first_interval
        nl, nh = second_interval
        
        return (nl <= el and nh >= el) or (nl >= el and nl <= eh)

    def is_lower(first_interval: List[int], second_interval: List[int]) -> List[int]:
        return first_interval[1] < second_interval[0]

    for index, interval in enumerate(intervals):
        if has_overalap(interval, new_interval): 
            new_interval = merge(interval, new_interval)
        
        else:
            if is_lower(new_interval, interval):
                res.append(new_interval)
                res.extend(intervals[index: ])
                return res
            else:
                res.append(interval)
    
    if new_interval:
        res.append(new_interval)
    return res

if __name__ == "__main__":
    print(insert_interval(intervals=[[1,3],[6,9]], new_interval=[2,5]))
    print(insert_interval(intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]], new_interval=[4,8]))
    print(insert_interval(intervals=[], new_interval=[5,7]))
    print(insert_interval(intervals=[[1, 5]], new_interval=[2,3]))
    print(insert_interval(intervals=[[2,5],[6,7],[8,9]], new_interval=[0,1]))