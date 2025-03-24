def extract(num):
    digits = []
    while num > 0: 
        digits.append(num % 10)
        num =  int(num / 10)
    
    digits = digits[::-1]
    print(digits)
    return digits

def count_digits(num):
    res = len(extract(num))
    print(f"count_digits({num}): {res}")
    return res

import math
def reverse(num):
    original = num
    reversed = 0

    while num > 0: 
        digit = num % 10
        num = int(num / 10)
        reversed = int(reversed * 10 + digit)

    print(f"reverse({original}): {reversed}")
    return reversed

if __name__ == "__main__":
    extract(950227)
    count_digits(29312)
    reverse(123)