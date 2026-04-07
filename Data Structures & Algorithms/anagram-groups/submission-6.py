class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strCode = defaultdict(list)
        for s in strs:
            sCode = ''.join(sorted(s))
            strCode[sCode].append(s)
        output = [] 
        for key in strCode:
            output.append(strCode[key])
        return output
            



    

    
    
