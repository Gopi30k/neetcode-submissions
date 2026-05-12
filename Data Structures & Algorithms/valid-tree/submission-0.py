from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)

            for nbr in adj[node]:
                if nbr == prev:
                    continue
                if not dfs(nbr, node):
                    return False
            return True
        
        if not dfs(0,-1):
            return False
        
        return len(visited) == n