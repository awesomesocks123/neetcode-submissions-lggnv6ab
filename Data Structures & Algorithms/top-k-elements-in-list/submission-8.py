class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #init count dict

        #match the count of each into buckets
        #buckets are array containing len(nums) + 1 places

        #buckets are empty lists
        #put counts to match index and item being the actual element

        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        buckets = []
        for _ in range(len(nums) + 1):
            buckets.append([])

        for element,count in freq.items():

            buckets[count].append(element)

        res = []
        for i in range(len(buckets) -1, 0, -1):
            if buckets[i]:
                for var in buckets[i]:
                    res.append(var)
                    if len(res) == k:
                        return res
                    
