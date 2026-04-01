from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        mem = [0 for i in range(len(nums))]

        @cache
        def dp(n, amount):
            if n >= len(nums):
                return amount
            if amount > mem[n]:
                mem[n] = amount
            
            return max(dp(n + 1, amount), dp(n + 2, amount + nums[n]))

        return dp(0, 0)



        