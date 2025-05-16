from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool: 
    course_map = dict()

    for course, prereq in prerequisites:
        if course in course_map:
            course_map[course].append(prereq)
        else:
            course_map[course] = [prereq]
    
    visited = set()
    
    def can_be_done(course):
        if course not in course_map: return True 
        if course in visited: return False 
        
        visited.add(course)
        for prereq in course_map[course]:
            
            if not can_be_done(prereq): return False
        
        visited.remove(course)
        course_map.pop(course)
        return True

    for i in range(num_courses):
        if not can_be_done(i): return False 
    return True 


if __name__ == "__main__":
    print(can_finish(2, [[1, 0]]))
    print(can_finish(2, [[1, 0], [0, 1]]))
    print(can_finish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]]))
    print(can_finish(5, [[1,4],[2,4],[3,1],[3,2]]))
    print(can_finish(4, [[0,1],[3,1],[1,3],[3,2]]))