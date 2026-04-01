class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low, high = max(weights), sum(weights)
        min_cap = high

        while low <= high:
            cur_cap = (low + high) // 2

            total = 0
            cur_days = 0

            for w in weights:
                if total + w > cur_cap:
                    total = w
                    cur_days += 1
                else:
                    total += w
            if total > 0:
                cur_days += 1
            
            if cur_days <= days:
                min_cap = min(min_cap, cur_cap)
                high = cur_cap - 1
            else:
                low = cur_cap + 1
        
        return min_cap

        
        

        
            


