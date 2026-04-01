class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        def backtrack(index, cur_set):
            if index >= len(nums):
                res.append(cur_set[:])
                return
            
            cur_set.append(nums[index])
            backtrack(index + 1, cur_set)
            cur_set.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            
            backtrack(index + 1, cur_set)

        backtrack(0, [])

        return res

        