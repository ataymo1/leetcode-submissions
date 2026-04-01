class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicates = set()
        l = 0
        duplicates.add(nums[0])
        for r in range(1, len(nums)):
            if r - l > k:
                duplicates.remove(nums[l])
                l += 1
            if nums[r] in duplicates:
                return True
            duplicates.add(nums[r])
        return False
        