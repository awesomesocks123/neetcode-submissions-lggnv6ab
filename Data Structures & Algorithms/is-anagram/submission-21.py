class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_countS = [0] * 26 
        freq_countT = [0] * 26 

        for char in s:
            position = ord('a') - ord(char)
            freq_countS[position] += 1 
        for char in t:
            position = ord('a') - ord(char)
            freq_countT[position] += 1

        return freq_countS == freq_countT 

