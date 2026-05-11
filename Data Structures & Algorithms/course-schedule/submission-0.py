
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)
        
        visited = set()
        path = set()
        
        def dfs(node):
            if node in path:
                return False        # cycle detected
            if node in visited:
                return True        # already confirmed safe
            
            path.add(node)         # add to current path
            
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False    # cycle found downstream
            
            path.remove(node)      # done with this path
            visited.add(node)         # mark as fully processed
            return True            # no cycle found
        
        for course in range(numCourses):
            if not dfs(course):
                return False        # cycle exists
        
        return True                # no cycle anywhere