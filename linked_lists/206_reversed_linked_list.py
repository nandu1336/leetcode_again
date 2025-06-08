from typing import Optional
from node import ListNode


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None

    while head:
        nex, head.next = head.next, prev
        prev, head = head, nex

    return prev


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = reverse_list(head)
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)