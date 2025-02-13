from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head:Optional[ListNode], n:int) -> Optional[ListNode]:
        cur = ListNode()
        cur.next = head
        first = second = cur
        for _ in range(n):
            second = second.next
        while second.next is not None:
            first = first.next
            second = second.next
        first.next = first.next.next
        return cur.next


head_list = [1,2,3,4,5]

def makeListNodeFromList(_list):
    temp = h = ListNode()
    for i in _list:
        temp.next = ListNode(i)
        temp = temp.next
    return h.next

headNode = makeListNodeFromList(head_list)
Solution.removeNthFromEnd(Solution(), headNode, 2)