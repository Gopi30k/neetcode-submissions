class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: [] for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""          # invalid: prefix rule violated

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break             # stop after first difference

        visited = {}                # char → True (in path) / False (done)
        result = []

        def dfs(char):
            if char in visited:
                return visited[char]          # True = cycle, False = already safe

            visited[char] = True     # mark as in current path

            for neighbor in adj[char]:
                if dfs(neighbor):
                    return True      # cycle found downstream

            visited[char] = False    # done, mark as safe
            result.append(char)      # append on finish
            return False              # no cycle

        for char in adj:
            if dfs(char):
                return ""          # cycle detected

        return "".join(reversed(result))