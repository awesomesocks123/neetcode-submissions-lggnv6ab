class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1 
        trapped_water, max_left, max_right = 0, 0, 0 
        while l < r: 
            if height[l] < height[r]:
                max_left = max(height[l],max_left)
                trapped_water += max_left - height[l]
                l += 1
            else:
                max_right = max(height[r], max_right)
                trapped_water += max_right - height[r]
                r -= 1
        return trapped_water