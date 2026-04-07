class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        max_L, max_R = 0 , 0 
        
        l,r = 0, len(height) - 1
        
        while l<r:
            if height[l] < height[r]:
                max_L = max(height[l],max_L)
                total_water += max_L - height[l]
                l += 1
            else:
                max_R = max(height[r], max_R)
                total_water += max_R - height[r] 
                r -= 1
                    
        return total_water