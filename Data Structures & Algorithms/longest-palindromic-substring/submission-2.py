from functools import cache
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        self.res = s[0]


        # add a new letter
        # remove a letter but go to the next
        @cache
        def dp(start, end):

            if isPalindrome(start, end):
                copy = s[start:end + 1]
                self.res = copy if len(copy) > len(self.res) else self.res
            
            if end + 1 >= len(s):
                return
            
            dp(start, end + 1)
            dp(start + 1,  end + 1)

        @cache
        def isPalindrome(start, end):

            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True


        dp(0, 1)
        return self.res


             

        


        