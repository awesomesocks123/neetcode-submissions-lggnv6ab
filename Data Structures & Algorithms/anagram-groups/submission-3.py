'''
Give an array of strings strs, group all anagrams together into a sublists
return the output in any order
- array of strings strs
- 1 <= strs.length <=1000 atleast 1 - 1000 in size 
- a string in the string array can be empty or up to 100 in terms of length
- strs[i] is all lower case letter ( dont need to worry about .isLower())



an anagram is a string that contains the exact same characters as another string.
But the order can be different. 

Return the output in anyorder
- must return an array
- the array must contain arrays of each string in the given array
- can be in anyorder when returned
- anagrams must be in the same array 

- how do we identify anagrams?
- check for same letters 
- check for same length 
- we can sort the string and get a number from it using ord


possible datastructures
- anagrams can be hashed into the same hash value 
- we can use a dictionary
- key = hashed value of the anagram, value = the array that contains the anagram
- keep appending to the array

- we use python lists

'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedDict = {}
        for s in strs:
            sorted_key = self.anagramKeys(s)
            if sorted_key in sortedDict:
                sortedDict[sorted_key].append(s)
            else:
                sortedDict[sorted_key] = [s]
        output = [] 
        for stringArrays in sortedDict.values():
            output.append(stringArrays)
        return output 

    def anagramKeys (self, string: str) -> int:
        anaSort = ''.join(sorted(string))
        charArray = []
        for s in anaSort:
            charArray.append(s)
        return ''.join(sorted(charArray))

