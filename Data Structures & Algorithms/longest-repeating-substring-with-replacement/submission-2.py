from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0 
        maxFreqCnt = 0
        for r in range(len(s)):
            maxFreqCnt = max(Counter(s[l : r + 1]).values())
            while (r - l + 1) - maxFreqCnt > k:
                l += 1
            res = max(res, r - l + 1)
        return res