import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        mod_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        s = 0
        e = len(mod_s) -  1
        while s < e:
            if mod_s[s] != mod_s[e]:
                return False
            s += 1
            e -= 1
        return True
        
