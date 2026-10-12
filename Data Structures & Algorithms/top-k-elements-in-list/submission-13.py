class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for n in nums:
            # if n in count:
            #     count[n] +=1
            # count[n] = 1 
            count[n] = count.get(n,0) + 1

        #key: value
        #element: count

        array = [ [] for _ in range(len(nums) + 1)]

        for key, value in count.items():
            array[value].append(key) 
        
        res = [] 

        for i in range(len(array) -1, 0 ,-1): 
            for count in array[i]:
                res.append(count)
                if len(res) == k:
                    return res
        return res 




        