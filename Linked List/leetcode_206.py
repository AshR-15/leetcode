from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     valList = []
    #     while head:
    #         valList.append(head.val)
    #         head = head.next
    #     valList.reverse()
    #     return self.listToListNode(valList)
    #
    # def listToListNode(lst):
    #     cur = dummy = ListNode()
    #     for l in lst:
    #         cur.next = ListNode(l)
    #         cur = cur.next
    #     return dummy.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        curr = head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

list = [1,2,3,4,5]

def listToListNode(lst):
    cur = dummy = ListNode()
    for l in lst:
        cur.next = ListNode(l)
        cur = cur.next
    return dummy.next

listNode = listToListNode(list)

solution = Solution.reverseList(Solution(), listNode)