class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False
        
        freq1 = [0] * 26
        freq2 = [0] * 26

        for c in s1:
            freq1[ord(c) - ord('a')] += 1

        for i in range(len(s1)):
            freq2[ord(s2[i]) - ord('a')] += 1
        
        if self.checkArray(freq1, freq2):
            return True
        L = 0

        for R in range(len(s1), len(s2)):
            freq2[ord(s2[L]) - ord('a')] -= 1
            freq2[ord(s2[R]) - ord('a')] += 1
            if self.checkArray(freq1, freq2):
                return True
            L += 1

        return False
    
    
    
    def checkArray(self, a1, a2):
        for i in range(len(a1)):
            if a1 != a2:
                return False
        return True



