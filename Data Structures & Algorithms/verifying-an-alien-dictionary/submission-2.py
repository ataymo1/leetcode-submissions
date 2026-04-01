class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        h_map = {}
        for i, c in enumerate(order):
            h_map[c] = i
        
        for i in range(len(words) - 1):
            count = 0
            word1, word2 = words[i], words[i+1]
            len1, len2 = len(word1), len(word2)
            maxCount = min(len1, len2)
            while count < maxCount and word1[count] == word2[count]:
                count += 1
            
            if count == maxCount:
                if len1 > len2:
                    return False
                continue
            
            if h_map[word1[count]] > h_map[word2[count]]:
                return False

        return True

