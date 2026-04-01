class Solution:
    def canPartition(self, nums: List[int]) -> bool:


        cache = dict()

        def partition(i, total1, total2):
            if tuple((i, total1, total2)) in cache:
                return cache[(i, total1, total2)]

            if i == len(nums):
                if total1 == total2:
                    return True
                else:
                    cache[(i, total1, total2)] = False
                    return False
            
            if partition(i + 1, total1 + nums[i], total2):
                return True
             
            if partition(i + 1, total1, total2 + nums[i]):
                return True

            return False
                


        if partition(0, 0, 0):
            return True
        return False
        