from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = nums.count(val)
        l = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1
            print(nums, i, l)
        return len(nums) - count


nums = [0,1,2,2,3,0,4,2]
solution = Solution()
print(solution.removeElement(nums, 2))
