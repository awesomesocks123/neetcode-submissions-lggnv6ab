class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suffix = [1] * n

        prefix = [1] * n

        result = [1] * n

        prod = 1
        for i in range(n):
            prefix[i] = prod 
            prod *= nums[i]  
            
        prod = 1 
        for i in range(n-1,-1,-1):
            suffix[i] = prod 
            prod *= nums[i] 

        for i in range(n):
            result[i] = suffix[i] * prefix[i]


        return result 