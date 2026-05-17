class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            # skip duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            L, R = i + 1, len(nums) - 1
            
            while L < R:
                total = nums[i] + nums[L] + nums[R]
                
                if total == 0:
                    result.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    # skip duplicates for L
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
                    # skip duplicates for R
                    while L < R and nums[R] == nums[R+1]:
                        R -= 1
                        
                elif total < 0:
                    L += 1
                else:
                    R -= 1
        
        return result
            