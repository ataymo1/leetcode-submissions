'''
base cases:
finished coin index, above amount, at amount

steps: take a coin, skip the coin

take a coin:
    amount - coin[i], index 

skip a coin:
    amount, index + 1

'''
from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @cache
        def dp(coin_index, total):
            if coin_index >= len(coins) or total < 0:
                return 0
            if total == 0:
                return 1
            
            return dp(coin_index, total - coins[coin_index]) + dp(coin_index + 1, total)
    
        return dp(0, amount)
            
    


        