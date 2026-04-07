class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i,j in enumerate(nums):
            diff = target - j
            if diff in s:
                return [s[diff],i]
            else:
                s[j] = i 