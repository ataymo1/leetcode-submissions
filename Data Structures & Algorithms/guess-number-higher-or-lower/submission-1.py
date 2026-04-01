# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        max_num = n
        min_num = 1
        while(True):
            mid = (max_num + min_num) // 2
            g = guess(mid)
            if g == -1:
                max_num = mid - 1
            elif g == 1:
                min_num = mid + 1
            else:
                return mid

        