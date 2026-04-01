class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        found = set()
        
        for num in nums[:]:
            if num in found:
                nums.remove(num)
            else:
                found.add(num)

        return len(nums)


        