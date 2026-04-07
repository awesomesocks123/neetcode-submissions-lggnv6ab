class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #lets check length first if lenghts aren't the same they're not anagrams
        if len(s) != len(t):
            return False
        #lets check each character
        # we can count characters and compare if the char count in each string
        # if the char count are the same then we have an anagram 

        countS, countT = {}, {}

        for ch in range(len(s)):
            countS[s[ch]] = countS.get(s[ch],0) + 1
            countT[t[ch]] = countT.get(t[ch],0) + 1
        print(countT, countS)
        return countT == countS

        