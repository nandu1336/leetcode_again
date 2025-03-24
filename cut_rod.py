prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
temp = []

def cut_rod(n: int):
    if n == 0: return 0
    for i in range(1, n):
        val = prices[i]
        val += cut_rod(n-i)
        temp.append(val)

    return max(temp) if temp else 0

if __name__ == "__main__":
    print(f"input: {4} || output: {cut_rod(4)}")