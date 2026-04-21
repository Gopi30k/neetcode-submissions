class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            counter = 0
            curr = n
            while curr in numSet:
                counter += 1
                curr += 1
            longest = max(counter, longest)
        return longest 