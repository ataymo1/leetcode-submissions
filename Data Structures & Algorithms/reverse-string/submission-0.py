class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L, R = 0, len(s) - 1
        while R > L:
            s[L], s[R] = s[R], s[L]
            R -= 1
            L += 1
        