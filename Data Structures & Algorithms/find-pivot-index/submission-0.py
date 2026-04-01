class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        leftTotal = 0
        rightTotal = sum(nums) - nums[0]
        if leftTotal == rightTotal:
            return 0
        
        for i in range(1, len(nums)):
            leftTotal += nums[i-1]
            rightTotal -= nums[i]
            if leftTotal == rightTotal:
                return i
        return -1




        