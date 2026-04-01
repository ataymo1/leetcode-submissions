class Solution:
    def mySqrt(self, x: int) -> int:

        low, high = 0, x
        res = 0

        while low <= high:
            mid = (low + high) // 2
            squared = mid * mid
            if squared == x:
                return mid
            elif squared > x:
                high = mid - 1
            else:
                low = mid + 1
                res = mid


        return res