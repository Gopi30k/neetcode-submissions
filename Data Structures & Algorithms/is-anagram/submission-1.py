class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {char: s.count(char) for char in s}
        t_dict={char: t.count(char) for char in t}
        return s_dict == t_dict
        