class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            # prefix sums 
            res = [1] * len(nums)
            prod = 1 
            for i in range(len(nums)):
                res[i] = prod 
                prod *= nums[i]
            print(res) 
            prod = 1 
            for i in range(len(nums)-1,-1,-1):
                res[i] *= prod
                prod *= nums[i]
            return res 

            