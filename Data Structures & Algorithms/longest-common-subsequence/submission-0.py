from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def dp(first, second):
            if not first or not second:
                return 0
            if first[0] == second[0]:
                return 1 + dp(first[1:], second[1:])

            return max(dp(first[1:], second[:]), dp(first[:], second[1:]))
        
        return dp(text1, text2)
