class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[1], nums[0])
        def dp(n):
            mem = [-1] * len(n)
            mem[0], mem[1] = n[0], max(n[0], n[1])

            for i in range(2, len(n)):
                mem[i] = max(mem[i-1], mem[i-2] + n[i])
            
            return mem[-1]
            

        # call this twice, 1st robbing the first house
        # skipping first house
        return max(dp(nums[1:]), dp(nums[:-1]))


        
        

            


        
        