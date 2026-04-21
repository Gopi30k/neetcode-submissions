class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for str in strs:
            count_arr = [0] * 26
            for c in str:
                count_arr[ord(c) - ord('a')] += 1
            anagram_dict[tuple(count_arr)].append(str)
        return list(anagram_dict.values())