class Solution:
    def isHappy(self, n: int) -> bool:

    
        seen = set()
        
        while n not in seen:
            total = 0
            seen.add(n)
            for c in str(n):
                total += int(c) * int(c)
            if total == 1:
                return True
            n = total
        return False

        

        

        