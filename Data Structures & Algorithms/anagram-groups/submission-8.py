class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # return empty list or list of 1 if size is 1 or less

        if len(strs) <= 1:
            return [strs]


        # make diction of lists
        # append to list of dictiory

        strs_sort = defaultdict(list)

        for string in strs:
            key = ''.join(sorted(string))
            strs_sort[key].append(string)

        res = []
        for values in strs_sort.values():
            res.append(values)
        return res





        #return values in the dictionary 