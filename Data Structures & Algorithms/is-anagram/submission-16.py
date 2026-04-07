class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for ch in range(len(s)):
            countS[s[ch]] = countS.get(s[ch], 0) + 1
            countT[t[ch]] = countT.get(t[ch], 0) + 1
        
        return countS == countT