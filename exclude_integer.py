import math 
def exclude_integer(limit: int):
    prev_val, values = 0, []

    while prev_val < limit: 
        cur_value = temp = prev_val + 1
        exponent = 0
        
        while temp > 0: 
            digit = temp % 10
            temp  = temp // 10
            
            if digit == 4:
                cur_value += math.pow(10, exponent)
                break
            
            exponent += 1
        
        prev_val = cur_value
        values.append(prev_val)
    
    return values, len(values)
    

if __name__ == "__main__":
    limit = 100
    res, count = exclude_integer(limit)
    print(f"input: {limit} || output: {count} || numbers: {res}")
