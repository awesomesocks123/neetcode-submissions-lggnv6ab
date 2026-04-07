class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = {} 

        left = 0 
        maxLen = 0

        for right in range(len(s)):
            #check if we have a duplicate 
            if s[right] in seen:
                #we move left up
                left = max(left, seen[s[right]] +1)
            
            maxLen = max(maxLen, right - left + 1) 
            seen[s[right]] = right
        return maxLen