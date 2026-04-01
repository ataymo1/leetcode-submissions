class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        # how many people trust him
        trusted_map = [0] * n

        # does this person trust someone
        truster_map = [0] * n

        for truster, trusted in trust:
            trusted_map[trusted - 1] += 1
            truster_map[truster - 1] = -1

        for i in range(1, n + 1):
            if trusted_map[i - 1] == n-1 and truster_map[i - 1] == 0:
                return i

        return -1



        

        