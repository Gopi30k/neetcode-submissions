import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        mod_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l = 0
        r = len(mod_s) -  1
        while l< r:
            if mod_s[l] != mod_s[r]:
                return False
            l += 1
            r -= 1
        return True
        
