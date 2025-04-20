from typing import List

def car_fleet(target: int, positions: List[int], speed: List[int]) -> int:
    car_fleets = rem = n = len(positions)
    if n == 1: return 1

    fleet_tracker = {}
    speed_tracker = {}
    completed = set()

    while rem > 0:

        for i in range(n):
            if i in completed: continue
            v = positions[i] + speed[i]
            positions[i] = v

            if v in fleet_tracker:
                fleet_tracker[v].add(i)
                
                if speed[i] > speed_tracker[v]:
                    speed[i] = speed_tracker[v] 
                
                else: 
                    for v in fleet_tracker[v]:
                        speed[v] = speed[i]
                        speed_tracker[v] = speed[i]

            else:
                fleet_tracker[v] = set([i])
                speed_tracker[v] = speed[i]

            if positions[i] > target:
                if positions[i] in fleet_tracker:
                    cars = fleet_tracker.pop(positions[i]) 
                    speed_tracker.pop(positions[i])
                    completed = completed.union(cars)
                    rem -= len(cars)
                    car_fleets -= 1
            print(f"{fleet_tracker}\n{speed_tracker}\n{positions}\nrem: {rem}\nfleets: {car_fleets}\n{'-'*40}")
            
    return car_fleets

if __name__ == "__main__":
    # target = 10
    # positions = [3]
    # speed = [3]
    # print(car_fleet(target, positions, speed))
    
    # target = 100
    # positions = [0,2,4]
    # speed = [4,2,1]
    # print(car_fleet(target, positions, speed))
    
    target = 12
    positions = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    print(car_fleet(target, positions, speed))

    # target = 10
    # positions = [8,3,7,4,6,5]
    # speed = [4,4,4,4,4,4]
    # print(car_fleet(target, positions, speed))
             