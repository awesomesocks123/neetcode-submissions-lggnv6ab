'''Given an integer array nums and an integer k
return the k most frequent elements within the array
return the top number of elements in accordance to whatever K is 
k = 2 = top 2 lements
k = 5 = top 5 elements and so on 
k is always greater than 1 
k will always be between the unique elements in the array 
answer is always unique
so theres not [1,2,2]
and it'll aways be within the nums array 

return the output in anyorder
could be [3,2] or [2,3] doesn't matter 



input: nums = [1,2,2,3,3,3], k = 2

output [2,3] 

1 <= nums.lenght <= 10^4 
-1000 <= nums[i] <=1000
i <= k <= number of distinct elements in nums 

to solve this we can use hashing to solve this 
we need a count of some sort
to count the number of occurence of each unique element
dictionary : {}
the key will be the element in the array being nums[i]
and the value is the count 

but how do we return k?
iterate through the dictionary and find the highest value and return the key?


'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCount = {}
        for n in nums:
            numsCount[n] = numsCount.setdefault(n, 0) + 1
        top_k = sorted(numsCount, key=numsCount.get, reverse=True)[:k]
        return top_k
            









