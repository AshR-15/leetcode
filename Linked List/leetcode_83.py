from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = head
        while head:
            temp = head.next
            if temp is None:
                break
            while temp and head.val == temp.val:
                temp = temp.next
            head.next = temp
            head = head.next
        return new_list


list1 = [1,1,2,3,3]
list1Node = ListNode()
head1 = list1Node

for i in list1:
    new = ListNode()
    head1.val = i
    head1.next = new
    head1 = new

solution = Solution.deleteDuplicates(Solution(), list1Node)
