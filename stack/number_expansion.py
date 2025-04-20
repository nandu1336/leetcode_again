def expand_and_clear_stack(stack, reps):
    temp = stack.pop()

    if temp == "(":
        temp = ""

        while stack:
            item = stack.pop()
            if item == ")": break
            temp += item
        
    return temp * reps

def foo(in_str):
    stack = []
    out = ""
    
    for index in range(len(in_str)-1 , -1, -1):
        char = in_str[index]

        if char.isdigit():
            stack.append(expand_and_clear_stack(stack, int(char)))
        else:
            stack.append(char)    

    while stack: 
        out += stack.pop()

    print(f"input: {in_str} || output: {out}")

if __name__ == "__main__":
    foo("3(ab)2c")
    foo("3(2(ab))")
    foo("2ab3d")
    foo("2(2dc2(eb)bc)")