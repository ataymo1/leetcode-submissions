class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        # everytime prices[r] < price[l] l = r
        # everytime prices[l] >= price[r] r++
        l = 0
        max_profit = 0

        for r in range(1, len(prices)):
            max_profit = max(max_profit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r

        return max_profit

            

