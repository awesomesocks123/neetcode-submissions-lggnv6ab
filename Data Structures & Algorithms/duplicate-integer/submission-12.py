class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = set()
        for n in nums:
            if n in h:
                return True
            else:
                h.add(n)
        return False