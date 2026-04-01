class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def backtracking(i, path, total):

            print(f"i: {i}, path: {path}, total: {total}")
            
            if total > target:
                return

            if total == target:
                res.append(path[:])
                return

            if i >= len(nums):
                return
            
            path.append(nums[i])
            backtracking(i, path, total + nums[i])
            path.pop()
            backtracking(i+1, path, total)

        backtracking(0, [], 0) 

        return res
            

            

                

        
        