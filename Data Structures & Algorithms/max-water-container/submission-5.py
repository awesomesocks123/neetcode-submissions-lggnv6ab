class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea, l, r = 0,0, len(heights) - 1

        while l < r:
            length = min(heights[l], heights[r])
            width = r - l
            area = length * width
            maxarea = max(maxarea,area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxarea