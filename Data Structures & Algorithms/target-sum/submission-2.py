class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        
        def dp(i, total, res):

            if i == len(nums):
                if total == target:
                    return res + 1
                return res

            res = dp(i + 1, total - nums[i], res)

            res = dp(i + 1, total + nums[i], res)

            return res

        return dp(0, 0, 0)
