class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        first, second, nth = 1, 1, 0

        for i in range(n-1):
            nth = first + second
            first = second
            second = nth
        
        return nth


        