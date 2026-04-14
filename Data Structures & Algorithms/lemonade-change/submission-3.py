class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        change = [0] * 2

        for bill in bills:
            if bill == 10:
                if change[0] < 1:
                    return False
                else:
                    change[0] -= 1
                    change[1] += 1
            elif bill == 20:
                if change[1] < 1:
                    if change[0] < 3:
                        return False
                    else:
                        change[0] -= 3
                else:
                    if change[0] < 1:
                        return False
                    change[1] -= 1
                    change[0] -= 1
            else:
                change[0] += 1
        
        return True

        