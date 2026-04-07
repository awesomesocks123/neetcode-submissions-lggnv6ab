class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += "%s%s%s" % (len(s),"#",s)
        return res 

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = []
        i = 0 
        while i < len(s):
            j = i 
            num = 0 
            while s[j] != '#':
                num = num*10  + int(s[j])
                j += 1
            j += 1
            k = j
            temp = ""
            while num > 0:
                temp += s[k]
                k += 1
                num -= 1
            res.append(temp)
            i = k 

        return res
