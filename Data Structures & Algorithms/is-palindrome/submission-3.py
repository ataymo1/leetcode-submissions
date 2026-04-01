class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        
        right = len(s) - 1

        for left in range(len(s)):
            if s[left] != s[right]:
                return False
            right -= 1;
        
        return True







