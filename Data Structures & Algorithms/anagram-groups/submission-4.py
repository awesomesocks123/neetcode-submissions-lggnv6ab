class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strCode = {}
        for s in strs:
            sCode = ''.join(sorted(s))
            if sCode not in strCode:
                strCode[sCode] = []
            strCode[sCode].append(s)
        output = [] 
        for key in strCode:
            output.append(strCode[key])
        return output
            



    

    
    
