class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_longest = 0

        for n in nums:
            if n - 1 not in nums_set:
                longest = 1
                while (n + longest) in nums_set:
                    longest += 1
                max_longest = max(longest, max_longest)
        return max_longest 