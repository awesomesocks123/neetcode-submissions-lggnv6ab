class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1 
        freq_array = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            freq_array[freq].append(num)

        output = [] 
        print(freq_array)
        for i in range(len(freq_array) -1,0,-1): 
            if len(freq_array[i]) > 0:
                output += freq_array[i]

        return output[:k]



        
