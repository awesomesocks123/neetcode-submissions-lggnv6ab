class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each word 
        # use the sorted word as the "key" 
        # the value will be the list
        # if key exists append the curr word into the value 
        # ex: stop =
        # sorted(stop) = "opst": ["stop", "pots", "tops"]

        # return res where we iterated over our entire dictioanry and just add the value 
        # res.append(key) 




        #idek how to start the bruteforce for this
        # instead of sort we can use the freq_array where we do freq = [0] * 26 

        #for each new word we make a freq array for 
        # def create_key[]
        # we can do sorted here 
        # or we can form the freq array here 

        #sorted will be onlogn
        #freq array will be o(n) 



        def create_key(word) -> str:
            #sorted() returns a new sorted list
            #a.sort() returns the list in sorted order 
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            return tuple(freq) 

        tracker = defaultdict(list)

        for word in strs:
            key = create_key(word)
            tracker[key].append(word)
        res = []
        for k,v in tracker.items():
            res.append(v) 
        return res 
