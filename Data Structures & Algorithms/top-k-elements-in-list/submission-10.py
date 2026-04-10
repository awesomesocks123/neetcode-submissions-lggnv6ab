class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n,0) + 1 
        
        buckets = [[]for _ in range(len(nums) + 1)]

        for key,val in freq.items():
            buckets[val].append(key) 
        
        res = []

        for i in range(len(buckets)-1,0,-1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res