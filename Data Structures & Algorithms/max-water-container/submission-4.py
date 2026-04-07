class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        mArea = 0
        while l < r:
            length = min(heights[r], heights[l])
            width = r - l 
            mArea = max((length * width), mArea)
            if heights[l] < heights[r]:
                l +=1
            else:
                r -= 1
        return mArea 