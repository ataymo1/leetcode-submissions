class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()

        def backtrack(index, cur_sum, cur_list):

            if cur_sum == target:
                res.append(cur_list[:])
                return
            
            if index >= len(candidates) or cur_sum > target:
                return
            
            cur_list.append(candidates[index])
            backtrack(index + 1, cur_sum + candidates[index], cur_list)
            cur_list.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            
            backtrack(index + 1, cur_sum, cur_list)
        
        backtrack(0, 0, [])

        return res



        