from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        count = 0
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def dfs(node):
            visited.add(node)

            for nbr in adj[node]:
                if nbr not in visited:
                    dfs(nbr)

        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)

        return count