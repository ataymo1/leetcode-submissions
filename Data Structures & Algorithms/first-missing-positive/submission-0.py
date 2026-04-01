class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        
        num_sum = sum(nums)
        negative = 0
        max_ = 0

        for i, num in enumerate(nums):
            max_ = max(max_, num)
            if num < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val-1] == 0:
                    nums[val-1] = -1 * (len(nums) + 1)
                elif nums[val-1] > 0:
                    nums[val-1] *= -1

        print(nums)
        
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        
        return max_ + 1









        