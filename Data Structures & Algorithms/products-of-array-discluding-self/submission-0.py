class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        i = 0
        while i < len(nums):
            pr = 1
            j = 0
            while j < len(nums):
                if i != j:
                    pr = pr * nums[j]
                j += 1
            out.append(pr)
            i += 1
        return out