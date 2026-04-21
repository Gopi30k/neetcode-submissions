class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict={}
        for i in range(0, len(s)):
            s_dict[s[i]] = s.count(s[i])
        for j in range(0, len(t)):
            t_dict[t[j]] = t.count(t[j])
        return s_dict == t_dict
        