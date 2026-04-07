class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {} 

        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0) + 1
        
        for c in t:
            if c not in count or count[c] == 0: 
                return False
            count[c] -= 1
        return True 