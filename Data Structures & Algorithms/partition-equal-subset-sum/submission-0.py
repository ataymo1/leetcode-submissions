class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def partition(i, total1, total2):
            if i == len(nums):
                if total1 == total2:
                    return True
                else:
                    return False
            
            if partition(i + 1, total1 + nums[i], total2):
                return True
             
            if partition(i + 1, total1, total2 + nums[i]):
                return True

            return False
                


        if partition(0, 0, 0):
            return True
        return False
        