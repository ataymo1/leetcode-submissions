class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N + 1)]
        rank = [1] * (N + 1)
        
        def find(n):
            if par[n] != n:
                par[n] = find(par[n])
            return par[n]
        
        def union(a, b):
            p1, p2, = find(a), find(b)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p2]

            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]



