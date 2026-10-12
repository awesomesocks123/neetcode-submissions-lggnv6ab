class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 

        freqT = [0] * 26 
        freqS = [0] * 26 
        for char in s:
            pos = ord(char) - ord('a')
            freqS[pos] += 1
        for char in t:
            pos = ord(char) - ord('a')
            freqT[pos] += 1
        
        return freqT == freqS 
