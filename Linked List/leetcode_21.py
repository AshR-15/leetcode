# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result_list = ListNode()
        head = result_list
        current1 = list1
        current2 = list2
        while current1 and current2 :
            if current1.val < current2.val:
                head.next = current1
                head = current1
                current1 = current1.next

            else:
                head.next = current2
                head = current2
                current2 = current2.next

        if current1 or current2:
            head.next = current1 if current1 else current2

        return result_list.next


list1 = [1,2,3]
list2 = [1,2,4]
list1Node = ListNode()
head1 = list1Node
list2Node = ListNode()
head2 = list2Node

for i in list1:
    new = ListNode()
    head1.val = i
    head1.next = new
    head1 = new

for i in list2:
    new = ListNode()
    head2.val = i
    head2.next = new
    head2 = new

solution = Solution.mergeTwoLists(Solution(), list1Node, list2Node)

check = solution

while check.next is not None:
    print(check.val)
    check = check.next
