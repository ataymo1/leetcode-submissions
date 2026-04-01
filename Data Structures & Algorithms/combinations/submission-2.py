class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def backtrack(cur_n, cur_nums):

            if len(cur_nums) == k:
                res.append(cur_nums[:])
                return

            if cur_n > n:
                return
        

            cur_nums.append(cur_n)
            backtrack(cur_n + 1, cur_nums)
            cur_nums.pop()

            backtrack(cur_n + 1, cur_nums)
        
        backtrack(1,[])

        return res
        