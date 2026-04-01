from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins:
            return -1

        @cache
        def dp(index, total, coin_amt):
            if total == 0:
                return coin_amt
            if index >= len(coins) or total < 0:
                return 1e9

            return min(dp(index, total - coins[index], coin_amt + 1), dp(index + 1, total, coin_amt))

        
        res = dp(0, amount, 0)

        if res == 1e9:
            return -1
        return res
        