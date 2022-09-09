class Solution:
    def climbStairs(self, n: int) -> int:
        result = 1
        prev = 1
        pre_prev = 0
        for i in range(n):
            result = prev + pre_prev
            pre_prev = prev
            prev = result
        return result