class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set1 = set(nums)
        s1 = len(set1)
        if s1 == len(nums) :
            return False
        return True
        

        


        
        