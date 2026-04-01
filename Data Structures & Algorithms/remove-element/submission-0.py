class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = 0

        for num in nums:
            if num != val:
                nums[L] = num
                L += 1
        
        return L 


        