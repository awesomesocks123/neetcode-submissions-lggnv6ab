class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mArea = 0
        l, r = 0, len(heights) - 1
        while l < r:
            mArea = max(mArea, (min(heights[l],heights[r])) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return mArea