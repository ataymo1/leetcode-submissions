class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        mem = [0 for i in range(len(nums))]
        mem[0], mem[1] = nums[0], max(nums[1], nums[0])

        for i in range(2, len(nums)):
            mem[i] = max(nums[i] + mem[i-2], mem[i-1])

        return mem[-1]



        