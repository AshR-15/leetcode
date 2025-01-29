from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointA = headA
        pointB = headB
        while pointA != pointB:
            pointA = pointA.next if pointA else headB
            pointB = pointB.next if pointB else headA
        return pointB


listA = [4,1,8,4,5]
listB = [5,6,1,8,4,5]
curA = dummyA = ListNode(0)
curB = dummyB = ListNode(0)

for e in listA:
    curA.next = ListNode(e)
    curA = curA.next

for e in listB:
    curB.next = ListNode(e)
    curB = curB.next

solution = Solution.getIntersectionNode(Solution(), dummyA.next, dummyB.next)

