class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [];

        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            target = abs(num)

            while r > l:
                total = nums[r] + nums[l]
                if total == target:
                    res.append([nums[r], nums[l], nums[i]])
                    l += 1
                    while r > l and nums[l] == nums[l-1]:
                        l += 1
                elif total > target:
                    r -= 1
                else:
                    l += 1
        
        return res
                

            

        



                    
