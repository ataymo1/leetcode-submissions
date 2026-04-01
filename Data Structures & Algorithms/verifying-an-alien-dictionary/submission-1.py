class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        h_map = {}
        for i, c in enumerate(order):
            h_map[c] = i
        
        for i in range(len(words) - 1):
            count = 0
            maxCount = min(len(words[i]), len(words[i+1]))
            while count < maxCount and words[i][count] == words[i+1][count]:
                count += 1
            
            if count == maxCount:
                if len(words[i+1]) < len(words[i]):
                    return False
                continue
            
            if h_map[words[i][count]] > h_map[words[i+1][count]]:
                return False

        return True

