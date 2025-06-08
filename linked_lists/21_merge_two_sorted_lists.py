from typing import Optional
from node import ListNode


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 and not list2: return
    
    head = res = ListNode()

    if list1.val < list2.val: 
        list1, list2 = list2, list1

    while list1 and list2:
        if list1.val < list2.val:    
            res.next = list1 
            list1 = list1.next

        else:
            res.next = list2
            list2 = list2.next

        res = res.next

    if list1:
        res.next = list1
    elif list2:
        res.next = list2
    
    return head.next


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    head = merge_two_lists(list1, list2)
    res = []

    while head:
        res.append(head.val)
        head = head.next 

    print(res)
