class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) 
        while low < high:
            midpoint = (high + low) // 2 
            if nums[midpoint] < target:
                low = midpoint + 1
            else:
                high = midpoint
        if low < len(nums) and nums[low] == target:
            return low
        else:
            return -1 