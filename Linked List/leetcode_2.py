from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = result = ListNode()
        head_l1 = l1
        head_l2 = l2
        carry = 0
        while head_l1 is not None and head_l2 is not None:
            if carry > 0:
                sum = head_l1.val + head_l2.val + carry
                carry = 0
            else:
                sum = head_l1.val + head_l2.val
            head_l1 = head_l1.next
            head_l2 = head_l2.next
            if len(str(sum)) > 1:
                carry = 1
                dummy.next = ListNode(sum%10)
            else:
                dummy.next = ListNode(sum)
            dummy = dummy.next
        while head_l1 is not None:
            if carry > 0:
                sum = head_l1.val + carry
                carry = 0
            else:
                sum = head_l1.val
            head_l1 = head_l1.next
            if len(str(sum)) > 1:
                carry = 1
                dummy.next = ListNode(sum%10)
            else:
                dummy.next = ListNode(sum)
            dummy = dummy.next
        while head_l2 is not None:
            if carry > 0:
                sum = head_l2.val + carry
                carry = 0
            else:
                sum = head_l2.val
            head_l2 = head_l2.next
            if len(str(sum)) > 1:
                carry = 1
                dummy.next = ListNode(sum % 10)
            else:
                dummy.next = ListNode(sum)
            dummy = dummy.next
        if carry == 1:
            dummy.next = ListNode(carry)
            dummy = dummy.next
        return result.next



l1_list = [9, 9, 9, 9, 9, 9, 9]
l2_list = [9, 9, 9, 9]


def makeLinkedList(_list):
    temp = h = ListNode()
    for l in _list:
        temp.next = ListNode(l)
        temp = temp.next
    return h.next


_l1 = makeLinkedList(l1_list)
_l2 = makeLinkedList(l2_list)

Solution.addTwoNumbers(Solution(), _l1, _l2)
