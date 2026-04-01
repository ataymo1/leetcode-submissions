'''
have as set with different characters, then our check inside the for-loop looks for the length of the set > k - 1
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, length = 0, 0
        replaced = defaultdict(int)
        max_freq = 0

        for R in range(len(s)):
            replaced[s[R]] += 1
            max_freq = max(max_freq, replaced[s[R]])

            while (R - L + 1) - max_freq > k:
                replaced[s[L]] -= 1
                L += 1
            
            length = max(length, R - L + 1)
        
        return length

        