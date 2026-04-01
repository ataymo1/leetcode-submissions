class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = {}
        visited = set()
        top = []

        for i in range(numCourses):
            adj[i] = []

        for course, pre in prerequisites:
            adj[course].append(pre)

        for i in range(numCourses):
            if not self.dfs(i, set(), visited, adj, top):
                return []
        
        return top

    def dfs(self, course, path, visited, adj, top):

        if course in path:
            return False
        if course in visited:
            return True
        
        visited.add(course)
        path.add(course)

        for pre in adj[course]:
            if not self.dfs(pre, path, visited, adj, top):
                return False
        
        top.append(course)
        path.remove(course)
        return True
        