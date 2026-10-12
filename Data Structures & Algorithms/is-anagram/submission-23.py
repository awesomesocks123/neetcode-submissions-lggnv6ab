class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqT = [0] * 26 
        freqS = [0] * 26 
        for char in s:
            pos = ord('a') - ord(char.lower())
            freqS[pos] += 1
        for char in t:
            pos = ord('a') - ord(char.lower())
            freqT[pos] += 1
        
        return freqT == freqS 
