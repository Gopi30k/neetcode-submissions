class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0 , len(heights)-1
        area = 0
        while l < r:
            w = r - l
            wh = min(heights[r] , heights[l])
            a = w * wh
            if a > area:
                area = a
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return area

            