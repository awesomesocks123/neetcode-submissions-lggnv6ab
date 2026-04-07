class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxCount = 0
        uniq = set()
        while r < len(s):
            while s[r] in uniq:
                uniq.remove(s[l])
                l += 1             
            uniq.add(s[r])
            maxCount = max(maxCount, r - l + 1)
            r += 1
        return maxCount 