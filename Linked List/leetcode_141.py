from typing import Optional

"""Two-Pointers Method (Floyd's Cycle-Finding Algorithm)"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        return False


list = [3, 2, 0, -4]
pos = 1
cur = dummy = ListNode(0)
for e in list:
    cur.next = ListNode(e)
    cur = cur.next

solution = Solution.hasCycle(Solution(), dummy.next)
print(solution)
