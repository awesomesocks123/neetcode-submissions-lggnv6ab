class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # this is a sliding window problem 

        # 1. Count frequencies
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # 2. Create buckets: index = frequency, value = list of numbers
        freq = []
        for _ in range(len(nums) + 1):
            freq.append([])
            
        for num, c in count.items():
            freq[c].append(num)
        # 3. Walk backwards from highest frequency to lowest
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res