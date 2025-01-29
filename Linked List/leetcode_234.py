from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        reverse = None
        while slow:
            tmp = slow.next
            slow.next = reverse
            reverse = slow
            slow = tmp
        first, second = head, reverse
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True


list = [1,2,2,1]

def listToListNode(lst):
    cur = dummy = ListNode()
    for l in lst:
        cur.next = ListNode(l)
        cur = cur.next
    return dummy.next

listNode = listToListNode(list)

solution = Solution.isPalindrome(Solution(), listNode)