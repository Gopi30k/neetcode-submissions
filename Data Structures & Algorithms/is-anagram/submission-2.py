class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict={}
        for s_char in s:
            s_dict[s_char] = s.count(s_char)
        for t_char in t:
            t_dict[t_char] = t.count(t_char)
        return s_dict == t_dict
        