class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        cache = dict()
        def dp(i, sum1, sum2):
            if tuple((i, sum1, sum2)) in cache:
                return cache[(i, sum1, sum2)]
            
            if i == len(stones):
                return abs(sum1 - sum2)
            
            cache[(i, sum1, sum2)] = min(dp(i+1, sum1 + stones[i], sum2), dp(i+1, sum1, sum2 + stones[i]))
            return cache[(i, sum1, sum2)]
            
        return dp(0, 0, 0)
                    

                


