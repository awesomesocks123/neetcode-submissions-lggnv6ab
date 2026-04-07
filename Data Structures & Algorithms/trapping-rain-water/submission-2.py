class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        
        # Compute left_max array
        max_left = 0
        for i in range(n):
            left_max[i] = max_left
            if height[i] > max_left:
                max_left = height[i]
        
        # Compute right_max array
        max_right = 0
        for i in range(n-1, -1, -1):
            right_max[i] = max_right
            if height[i] > max_right:
                max_right = height[i]
        
        # Calculate the trapped water
        total_water = 0
        for i in range(n):
            water = min(left_max[i], right_max[i]) - height[i]
            if water > 0:
                total_water += water
        
        return total_water