class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minV = float("inf")
        while l <= r:
            print("l", l, nums[l])
            print("r", r, nums[r])
            mid = (l+r) // 2
            print("mid",mid, nums[mid])

            print("minV",minV)
            if nums[l] <= nums[mid]:
                minV = min(minV, nums[l])
                l = mid + 1
            else:
                minV = min(minV, nums[mid])
                r = mid - 1
        return minV