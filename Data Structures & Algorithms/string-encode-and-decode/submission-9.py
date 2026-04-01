class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "";
        sol = "";
        for s in strs:
            sol += "&&&" + s;
        return sol;

    def decode(self, s: str) -> List[str]:
        if not s:
            return [];
        return list(s[3:].split("&&&"));
