class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        smallestWord = min(strs, key=len)
        for i in range(len(smallestWord)):
            res += smallestWord[i]
            for s in strs:
                print(res)
                if res not in s:
                    return res[:-1]

        return res

            

        