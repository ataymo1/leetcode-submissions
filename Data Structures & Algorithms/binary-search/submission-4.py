class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        while l <= r:
            midpoint = (l + r) // 2
            print(midpoint)
            val = nums[midpoint]
            print(val)
            
            if val == target:
                return midpoint
            elif val < target:
                l = midpoint + 1
            else:
                r = midpoint - 1

        return -1

        