

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i: i+len(needle)] == needle:
                return i
        return -1
    # def strStr(self, haystack: str, needle:str) -> int:
    #     lenH = len(haystack)
    #     lenN = len(needle)
    #     if lenN > lenH:
    #         return -1
    #     for i in range(lenH):
    #         sum_haystack = self.same(haystack[i:(i+lenN)], needle)
    #         print(haystack[i:(i+lenN)])
    #         if sum_haystack == True:
    #             return i
    #         if (lenH - i) <= lenN:
    #             break
    #     return -1
    #
    # def same(self, h: str, n:str) -> bool:
    #     for i in range(len(h)):
    #         if h[i] != n[i]:
    #             return False
    #     return True

_haystack = "leetcode"
_needle = "leeto"

sol = Solution()
print(sol.strStr(_haystack, _needle))