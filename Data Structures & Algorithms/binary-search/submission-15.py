class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        while l <= h:
            midpoint = (l + h) // 2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                l = midpoint + 1
            elif nums[midpoint] > target:
                h = midpoint - 1
        if nums[midpoint] != target:
            return -1
        return midpoint 