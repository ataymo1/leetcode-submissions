class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        cache = dict()
        
        def dp(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                return 0

            cur = dp(i + 1, total - nums[i]) + dp(i + 1, total + nums[i])
            
            return cur

        return dp(0, 0)
