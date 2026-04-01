class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        sol = 0

        for i in range(len(nums)):
            sol ^= nums[i]

        return sol

        