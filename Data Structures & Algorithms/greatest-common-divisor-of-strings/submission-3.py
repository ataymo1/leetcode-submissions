import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        GCD = ""
        length1, length2 = len(str1), len(str2)
        for i in range(1, min(length1, length2) + 1):
            if length1 % i != 0 or length2 % i != 0:
                continue
            test = str1[:i]

            if test * (length1 // i) == str1 and test * (length2 // i) == str2:
                GCD = test
        
        return GCD




            