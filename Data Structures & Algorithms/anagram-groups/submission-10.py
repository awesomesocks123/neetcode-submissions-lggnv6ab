# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


#         #use a dictionary 
#         #sorted form is the key 
#         #value is going to be a list 
#         #if key exists we dict.get[key].append(curr) 
#         #can initialize the dictonary as empty lists 

#         anagrams = defaultdict(list) 

#         for word in strs:
#             key = word.sort() 
#             if word in anagrams:
#                 anagrams.get(key).append(word)
#         res = [] 
#         for k,v in anagrams:
#             res.append(v)
#         return res 

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) 

        for word in strs:
            key = "".join(sorted(word))
            anagrams[key].append(word)
            
        return list(anagrams.values())

