# iderate (e):
#     if e is greater than cur_min
#         if greater than max
#             set as max
#     else
#         if profit made (max - min)
#             add to total
#         set min to cur
#         set max to cur

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min, cur_max = prices[0], prices[0]
        total = 0

        for price in prices:
            if price > cur_max:
                cur_max = price
            elif price < cur_max:
                profit = cur_max - cur_min
                if profit > 0:
                    total += profit
                cur_min = price
                cur_max = price
        
        if cur_min < cur_max:
            total += cur_max - cur_min
        return total

        