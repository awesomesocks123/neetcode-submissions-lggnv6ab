class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for n in range(len(nums)):
            diff = target - nums[n]
            if diff in map:
                return [map[diff],n]
            map[nums[n]] = n 