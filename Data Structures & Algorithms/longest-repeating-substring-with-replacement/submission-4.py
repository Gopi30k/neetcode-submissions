from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0 
        maxFreqCnt = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreqCnt = max(maxFreqCnt, count[s[r]])
            while (r - l + 1) - maxFreqCnt > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res