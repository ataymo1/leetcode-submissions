class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_nums = [0] * len(nums) * 2

        for i in range(len(new_nums)):
            new_nums[i] = nums[i % len(nums)]
        
        return new_nums
        