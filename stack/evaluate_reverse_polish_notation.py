from typing import List 
def evalutate(tokens: List):
    operators = set(["+", "-", "*", "/"])
    operands = []

    for token in tokens:
        if token in operators:
            op2 = operands.pop()
            op1 = operands.pop()
            res = int(eval(f"{op1} {token} {op2}"))
            operands.append(res)
        else:
            operands.append(token)
    return operands.pop()

if __name__ == "__main__":
    # print(evalutate(tokens=["2","1","+","3","*"]))
    print(evalutate(tokens=["4","13","5","/","+"]))