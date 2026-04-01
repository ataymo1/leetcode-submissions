class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        element = None
        counter = 0
        
        for num in nums:
            if counter == 0:
                element = num
            counter += 1 if num == element else -1
        
        return element



        