from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        have = 0 
        tCount = Counter(t)
        need = len(tCount)
        l = 0
        windowCounter = {}
        resLen = float('inf')
        res = [-1, -1]
        for r in range(len(s)):
            c = s[r]
            windowCounter[c] = windowCounter.get(c,0) + 1
            if c in t and windowCounter[c] == tCount[c]:
                have += 1
            while have == need:
                if (r-l+1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                windowCounter[s[l]] -= 1
                if s[l] in tCount and windowCounter[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float('inf') else ""