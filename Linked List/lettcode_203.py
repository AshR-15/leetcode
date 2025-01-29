from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        result = current = ListNode()
        h = head
        while h:
            if h.val != val:
                current.next = h
                current = current.next
            h = h.next
        return result.next

list = [1,2,6,3,4,5,6]
val = 6

def listToListNode(lst):
    cur = dummy = ListNode()
    for l in lst:
        cur.next = ListNode(l)
        cur = cur.next
    return dummy.next

listNode = listToListNode(list)
solution = Solution.removeElements(Solution(), listNode, val)