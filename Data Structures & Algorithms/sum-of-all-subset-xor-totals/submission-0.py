class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        total = []

        def backtrack(i, cur_xor):
            if i >= len(nums):
                total.append(cur_xor)
                return
            
            cur_xor ^= nums[i]
            backtrack(i + 1, cur_xor)
            cur_xor ^= nums[i]

            backtrack(i + 1, cur_xor)

        backtrack(0, 0)
        return sum(total)
            

            
            
            


        