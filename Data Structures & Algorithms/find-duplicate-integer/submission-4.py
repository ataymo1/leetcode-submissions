class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast = 0, 0

        while(True):
            if nums[slow % len(nums)] == nums[fast % len(nums)] and (slow % len(nums)) != (fast & len(nums)):
                return nums[fast % len(nums)]
            fast += 2
            slow += 1


        