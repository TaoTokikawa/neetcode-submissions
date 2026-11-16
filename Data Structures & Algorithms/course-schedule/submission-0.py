class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        groups = defaultdict(list)
        for a, b in prerequisites:
            groups[a].append(b)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        def dfs(i):
            if states[i] == VISITING:
                return False
            elif states[i] == VISITED:
                return True
            
            states[i] = VISITING

            for neighbor in groups[i]:
                if not dfs(neighbor):
                    return False
            
            states[i] = VISITED
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True