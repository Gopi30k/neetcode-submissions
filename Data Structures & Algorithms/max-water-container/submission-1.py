class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        for l in range(0,len(heights)):
            r = l + 1
            while r < len(heights):
                w = r - l
                # print("W", w)
                wh = min(heights[l], heights[r])
                # print("wh", wh)
                a = w * wh
                # print("a", a)
                if a > area:
                    area = a
                r+=1
        return area

