class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = defaultdict(list)

        # add each string to corresponded group
        for s in strs:
            grp["".join(sorted(s))].append(s)
        
        return list(grp.values())