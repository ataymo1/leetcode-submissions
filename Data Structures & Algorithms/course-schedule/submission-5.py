class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites:
            return True
        
        adj = {}
        visited = set()

        for i in range(numCourses):
            adj[i] = []
        
        for course, pre in prerequisites:
            adj[course].append(pre)

        for i in range(numCourses):
            if not self.bfs(i, [], visited, adj):
                return False
        
        return True

    def bfs(self, course, path, visited, adj):
        if course in path:
            return False
        if course in visited:
            return True
        
        visited.add(course)
        path.append(course)

        for pre in adj[course]:
            if not self.bfs(pre, path, visited, adj):
                return False
        
        path.pop()

        return True

        
            

        






        