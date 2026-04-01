class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums))]
        postfix = [1 for _ in range(len(nums))]

        total = 1
        for i in range(1, len(nums)):
            total *= nums[i-1] 
            prefix[i] = total
        
        total = 1
        for i in range(len(nums) - 2, -1, -1):
            total *= nums[i+1] 
            postfix[i] = total

        res = [0 for _ in range(len(nums))]

        for i in range(len(res)):
            res[i] = prefix[i] * postfix[i]
        
        return res
