class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        L, max_len = 0, 0

        substring = set()

        for R in range(len(s)):
            while s[R] in substring:
                substring.remove(s[L])
                L += 1
            else:
                substring.add(s[R])
                max_len = max(max_len, R - L + 1)
        
        return max_len



