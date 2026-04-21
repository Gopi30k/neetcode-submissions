class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_d = {}
        for str in strs:
            temp_str = ''.join(sorted(str))
            sorted_d.setdefault(temp_str, []).append(str)
        return list(sorted_d.values())
