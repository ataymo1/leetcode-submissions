class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            element = nums[mid]

            if element == target:
                return mid
            elif element > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return l


        