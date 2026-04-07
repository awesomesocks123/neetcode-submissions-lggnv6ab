class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1 
        while low <= high:
            midpoint = low + ((high - low) // 2)
            if nums[midpoint] < target:
                low = midpoint + 1
            elif nums[midpoint] > target:
                high = midpoint - 1
            else:
                return midpoint 
        return -1 