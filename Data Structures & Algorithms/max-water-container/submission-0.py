class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_vol = min(heights[l], heights[r]) * (r - l)
        while l < r:
            if (heights[l] > heights[r]):
                r -= 1
            else:
                l += 1
            
            vol = min(heights[l], heights[r]) * (r - l)
            if vol > max_vol:
                max_vol = vol

        return max_vol

                