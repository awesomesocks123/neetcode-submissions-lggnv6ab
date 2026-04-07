class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        result = []
        for s in strs:
            sortedKey = ''.join(self.sortedKey(s))
            if sortedKey in dict:
                dict[sortedKey].append(s)
            else:
                dict[sortedKey] = [s]
        for value in dict.values():
            result.append(value)
        return result

                
    
    def sortedKey(self, string: str) -> [str]:
        charArray = []
        for c in string:
            charArray.append(c.lower())
        return ''.join(sorted(charArray))


    

    
    
