from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2:Optional[ListNode]):
        result = head = ListNode()
        head1 = list1
        head2 = list2
        while head1 and head2:
            if head1.val < head2.val:
                head.next = head1
                head = head.next
                head1 = head1.next
            else:
                head.next = head2
                head = head.next
                head2 = head2.next
        if head1:
            head.next = head1
        if head2:
            head.next = head2
        return result.next

list1 = [1,2,4]
list2 = [1,3,4]

def listToListNode(lst):
    cur = dummy = ListNode()
    for l in lst:
        cur.next = ListNode(l)
        cur = cur.next
    return dummy.next

listNode1 = listToListNode(list1)
listNode2 = listToListNode(list2)

solution = Solution.mergeTwoLists(Solution(), listNode1, listNode2)