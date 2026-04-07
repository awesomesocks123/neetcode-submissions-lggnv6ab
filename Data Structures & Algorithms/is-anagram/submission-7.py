class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {} #s
        j = {} #t
        if (len(s)) != (len(t)):
            return False
        for string in s:
            h[string] = h.get(string,0) + 1
        for tring in t:
            j[tring] = j.get(tring,0) +1 
        return h == j