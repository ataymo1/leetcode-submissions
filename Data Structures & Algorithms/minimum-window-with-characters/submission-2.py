class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        original = defaultdict(int)
        counter = defaultdict(int)
        comparer = defaultdict(int)
        
        total = len(t)
        
        for c in t:
            original[c] += 1

        res = ""

        L = 0
        for R in range(len(s)):
            addletter = s[R]
            if addletter in original:
                if addletter in comparer:
                    if comparer[addletter] < original[addletter]:
                        comparer[addletter] += 1
                else:
                    comparer[addletter] += 1
                counter[addletter] += 1

        
            while L <= R and original == comparer:
                if not res or len(res) > R - L:
                    res = s[L:R+1]
                removeletter= s[L]
                if removeletter in counter:
                    if counter[removeletter] <= comparer[removeletter]:
                        comparer[removeletter] -= 1
                    counter[removeletter] -= 1
                L += 1
        
        return res
            

        
        