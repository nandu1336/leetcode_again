from typing import Optional
from node import ListNode


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
    slow = fast = head 

    while fast and fast.next and n != 0:
        fast = fast.next 
        n -= 1

    while fast.next:
        slow = slow.next
        fast = fast.next
    
    if n != 0: return head.next
    slow.next = slow.next.next if slow.next else None 
    return head

if __name__ == "__main__":
    head = remove_nth_from_end(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
    # head = remove_nth_from_end(ListNode(1), 1)
    # head = remove_nth_from_end(ListNode(1, ListNode(2)), 2)
    res = []

    while head:
        res.append(head.val)
        head = head.next

    print(res)