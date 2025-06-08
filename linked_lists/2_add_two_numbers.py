from typing import Optional
from node import ListNode


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    res = ListNode()
    dummy = res
    carry = 0

    while l1 or l2:
        val = carry
        val += l1.val if l1 else 0
        val += l2.val if l2 else 0
    
        carry = val // 10
        val = val % 10

        l1 = l1.next if l1 else None 
        l2 = l2.next if l2 else None 
        res.next = ListNode(val)
        res = res.next
    if carry: res.next = ListNode(carry)
    return dummy.next

if __name__ == "__main__":
    # l1 = ListNode(2, ListNode(4, ListNode(3)))
    # l2 = ListNode(5, ListNode(6, ListNode(4)))

    # l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    # l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

    l1 = ListNode(2, ListNode(4, ListNode(9)))
    l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))
    l3 = add_two_numbers(l1, l2)

    res = []
    while l3:
        res.append(l3.val)
        l3 = l3.next 

    print(res)