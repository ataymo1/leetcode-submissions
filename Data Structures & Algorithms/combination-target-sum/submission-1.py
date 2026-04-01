class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        length = len(nums)

        def backtrack(index, cur_nums, cur_sum):

            print(f"{cur_nums} : {cur_sum}")
            if cur_sum == target:
                res.append(cur_nums[:])
                return

            if cur_sum > target or index >= length:
                return

            for i in range(index, length):
                cur_nums.append(nums[i])
                backtrack(i, cur_nums, cur_sum + nums[i])
                cur_nums.pop()



        backtrack(0, [], 0)
        return res
            

            

                

        
        