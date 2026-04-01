class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N + 1)]
        
        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(a, b):
            p1, p2, = find(a), find(b)

            if p1 == p2:
                return False
            
            par[p1] = p2

            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]