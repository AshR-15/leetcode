class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd = 0
        if low % 2 != 0:
            odd += 1
        elif high % 2 != 0:
            odd += 1
        odd += int((high - low)/2)
        return odd

