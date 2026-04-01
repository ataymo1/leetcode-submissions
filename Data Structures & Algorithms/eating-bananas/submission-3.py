class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        least, greatest = 1, max(piles)
        min_rate = greatest

        while least <= greatest:
            hours = 0
            k = (least + greatest) // 2
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours > h:
                least = k + 1
            elif hours <= h:
                greatest = k - 1
                min_rate = min(min_rate, k)
        
        return min_rate
            