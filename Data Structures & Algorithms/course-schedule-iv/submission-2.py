class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj = {}
        prereqs = {}

        for i in range(numCourses):
            adj[i] = set()
            prereqs[i] = set()
        
        for pre, course in prerequisites:
            adj[course].add(pre)

        for i in range(numCourses):
            if not prereqs[i]:
                self.dfs(i, prereqs, adj)
        
        answers = [0 for _ in range(len(queries))]
        
        for i in range(len(queries)):
            pre, course = queries[i]
            answers[i] = pre in prereqs[course]

        return answers

    
    def dfs(self, course, prereqs, adj):

        if prereqs[course]:
            return prereqs[course]

        for pre in adj[course]:
            prereqs[course].add(pre)
            prereqs[course].update(self.dfs(pre, prereqs, adj))
        
        return prereqs[course]

        





            

        
        