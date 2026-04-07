class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sums = {}

        for i, item in enumerate(nums):
            diff = target - item
            if diff in sums:
                return([sums[diff],i])
            else:
                sums[item] = i