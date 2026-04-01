class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        first, second = 1, 1

        for i in range(n-1):
            temp = second
            second = first + second
            first = temp
        
        return second


        