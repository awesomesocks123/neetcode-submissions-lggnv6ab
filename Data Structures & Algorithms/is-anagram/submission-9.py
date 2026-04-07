class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            ss = {}
            tt = {}
            for c in s:
                if c in ss:
                    ss[c] += 1
                else:
                    ss[c] = 1 
            for x in t:
                if x in tt:
                    tt[x] += 1
                else:
                    tt[x] = 1 
            if tt == ss:
                return True
            else:
                return False
        else:
            return False 

