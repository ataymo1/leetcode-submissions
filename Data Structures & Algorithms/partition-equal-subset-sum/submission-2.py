class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2
        length = len(nums)


        dp = [[False] * (target + 1) for _ in range(length + 1)]

        # initalizing first column to true (because if the target was 0 we dont have to take anything)
        for i in range(len(dp)):
            dp[i][0] = True
        
       
        for i in range(1, length + 1): # i represents using the first i elements (1 indexed)
            for t in range(1, target + 1): # t represents the current target sum
                current_num = nums[i-1]
                skip = dp[i-1][t]

                if current_num <= t: # if we can take the element
                    take = dp[i-1][t-current_num]
                    dp[i][t] = take or skip
                else:
                    dp[i][t] = skip

        return dp[length][target]

                



