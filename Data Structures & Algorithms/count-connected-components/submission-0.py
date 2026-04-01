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

        if n1 == n2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        res = 0
        unionFind = UnionFind(n)
        found = set()


        for n1, n2 in edges:
            unionFind.union(n1, n2)
        
        for i in range(n):
            leader = unionFind.find(i)
            if leader not in found:
                res += 1
                found.add(leader)

        return res
            



        