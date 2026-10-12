class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # account for length

        if len(s) != len(t):
            return False 

        freqT = [0] * 26
        freqS = [0] * 26 

        for char in s:
            #position = ord(char) - ord('a') 
            freqS[ord(char) - ord('a') ] += 1
        for char in t:
            freqT[ord(char) - ord('a') ] += 1
        return freqT == freqS 
            