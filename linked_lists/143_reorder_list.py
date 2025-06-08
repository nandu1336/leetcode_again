from typing import Optional
from node import ListNode


def reorder_list(head: Optional[ListNode]) -> None: 
    if not head.next: return head 
    nodes = []

    while head:
        nodes.append(ListNode(head.val))
        head = head.next
        
    n = len(nodes)
    head = res = ListNode()

    i, j = 0, n - 1

    while i < j:
        head.next = nodes[i]
        head.next.next = nodes[j]

        i += 1
        j -= 1
        head = head.next.next
    
    return res.next

def reorder_list_inplace(head: Optional[ListNode]) -> None:
    # find mid-point to break the list 
    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    new_list = slow.next
    slow.next = None 
    
    # reverse the linked list form the slow node
    prev = None
    while new_list:
        nex, new_list.next = new_list.next, prev
        prev, new_list = new_list, nex

    list1, list2 = head, prev
    
    # merge two lists
    while list1 and list2:
        l1_nex, l2_nex = list1.next, list2.next
        
        list1.next = list2
        list2.next = l1_nex

        list1, list2 = l1_nex, l2_nex
    
    return head



if __name__ == "__main__":
    head = reorder_list_inplace(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
    res = []
    
    while head:
        res.append(head.val)
        head = head.next

    print(res)

