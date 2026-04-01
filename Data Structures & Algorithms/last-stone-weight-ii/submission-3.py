class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        cache = dict()
        def dp(i, sum1, sum2):
            index = tuple((i, sum1, sum2))
            if index in cache:
                return cache[index]
            
            if i == len(stones):
                return abs(sum1 - sum2)
            
            cache[index] = min(dp(i+1, sum1 + stones[i], sum2), dp(i+1, sum1, sum2 + stones[i]))
            return cache[index]
            
        return dp(0, 0, 0)
                    

                


