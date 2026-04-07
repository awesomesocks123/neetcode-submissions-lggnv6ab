class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        still finding minimum aka smallest 

        [1,2,3,4,5,6] but array is rotated so 
        [1,2,3,4,5,6] -> [3,4,5,6,1,2] rotated 4 times
         ->1
           ->1
             ->1
               ->1,2
         3 4 5 6 1 2
         |         |
         left.    right
         0 + 2 + 1 = 3

         mid = 5 right = 2

         5 > 2? no 
         left = mid + 1
         3 + 5 = 8
         8/ 2 
         4 
        1 < 2?




         even if its rotated its still in sorted / monotonic state 

         we know forsure numbers on the right side should be greater than numbers on the left side

         so if we land on a mid point on our right side and its less than whatever is on our left 
        
         - we know to move left up once
        
        to find the smallest element we're looking for when its greatest/max
        and the minimum should be to the right of that element 
        
        """
        minimum = nums[0] 

        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            # check our condition here 
            if nums[mid] > nums[right]: 
                left = mid + 1 
            else:
                minimum = min(nums[mid],minimum)
                right = mid - 1
    

        return minimum



