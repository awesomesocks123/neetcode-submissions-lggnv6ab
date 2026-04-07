class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h = {}
        z = {}
        for i in s:
            h[i] = h.get(i, 0) + 1
        for j in t:
            z[j] = z.get(j, 0) + 1
        return h == z
        
