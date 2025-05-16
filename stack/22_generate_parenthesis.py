from typing import List 


def generate_parenthesis(n: int) -> List[str]: 
    res = []
    
    def inner(cur=[], oc=0, cc=0):
        if oc == cc == n:
            res.append("".join(cur))
            return

        if oc < n:
            cur.append("(")
            inner(cur, oc + 1, cc)
            cur.pop()

        if oc == n or cc < oc:            
                cur.append(")")
                inner(cur, oc, cc + 1)
                cur.pop()
            
    inner()
    return res

if __name__ == "__main__":
    print(generate_parenthesis(3))