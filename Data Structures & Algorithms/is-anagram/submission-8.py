class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        o = {}
        if len(s) != len(t):
            return False 

        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for n in t:
            if n in o:
                o[n] += 1
            else:
                o[n] = 1
        return d == o