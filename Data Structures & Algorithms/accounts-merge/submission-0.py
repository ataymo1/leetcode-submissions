from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, n):
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return self.par[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        unionFind = UnionFind(len(accounts))
        emailToAccount = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAccount:
                    unionFind.union(i, emailToAccount[email])
                else:
                    emailToAccount[email] = i
        
        emailGroups = defaultdict(list)
        for email, account in emailToAccount.items():
            leader = unionFind.find(account)
            emailGroups[leader].append(email)
        
        res = []
        for i, e in emailGroups.items():
            res.append([accounts[i][0]] + sorted(emailGroups[i]))

        return res




        
       