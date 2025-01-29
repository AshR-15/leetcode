from typing import List


class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     length = len(nums)
    #     for i in range(length):
    #         j = i+1
    #         while j < length and nums[i] == nums[j] and nums[i] != "_":
    #             nums.pop(i)
    #             nums.append("_")
    #         if nums[j] == "_":
    #             break
    #     return length - nums.count("_")
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                print(l, r, nums)
                nums[l] = nums[r]
                l += 1
                print(l, r, nums)
        return l

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# nums = [1, 1, 2]

solution = Solution.removeDuplicates(Solution(), nums)
print(solution)
