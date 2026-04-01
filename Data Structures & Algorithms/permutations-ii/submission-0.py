class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        perms = [[]]
        nums.sort()

        for i, n in enumerate(nums):
            nextPerms = []
            perms_set = set()
            for p in perms:
                for i in range(len(p) + 1):
                    pcopy = p.copy()
                    pcopy.insert(i, n)
                    checker = tuple(pcopy)
                    if checker not in perms_set:
                        nextPerms.append(pcopy)
                        perms_set.add(checker)
            perms = nextPerms
        
        return perms



        