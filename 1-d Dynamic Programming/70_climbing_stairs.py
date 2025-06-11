def climb_stairs(n: int) -> int: 

    def inner(n, cache={}):
        if n <= 1: 
            cache[n] = 1
            return 1
        
        if n in cache: return cache[n]

        return inner(n-1, cache)+ inner(n-2, cache)

    return inner(n)


if __name__ == "__main__":
    print(climb_stairs(3))
    print(climb_stairs(2))