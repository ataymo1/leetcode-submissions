class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def backtrack(cur_n, cur_nums):
            
            if len(cur_nums) == k:
                res.append(cur_nums[:])
                return

            for i in range(cur_n, n+1):
                cur_nums.append(i)
                backtrack(i + 1, cur_nums)
                cur_nums.pop()

        
        backtrack(1,[])

        return res
        