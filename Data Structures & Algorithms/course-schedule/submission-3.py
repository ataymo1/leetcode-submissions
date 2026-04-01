class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites:
            return True
        hmap = {}
        
        for i in range(numCourses):
            hmap[i] = []
        
        for a, b in prerequisites:
            hmap[a].append(b)

        def has_cycle(i, visited):
            if i in visited:
                return True
            visited.add(i)

            for neighbor in hmap[i]:
                if has_cycle(neighbor, visited):
                    return True
            visited.remove(i)
            return False
            

        for i in range(numCourses):
            if has_cycle(i, set()):
                return False
        return True

        






        