from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        f = 0
        temp = nums2[0]
        if n > 0:
            for i in range((m + n)-1, -1, -1):
                # if
                # print(i-m, i-n)
                print(i)
                # if nums1[i-m] > nums2[i-n]:




nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 2
sol = Solution()
sol.merge(nums1, m, nums2, n)
