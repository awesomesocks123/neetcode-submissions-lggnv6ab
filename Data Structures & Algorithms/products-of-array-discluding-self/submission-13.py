class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * (len(nums))
        pre = post = 1
        for n in range(len(nums)):
            out[n] = pre
            pre *= nums[n]
        for n in range(len(nums)-1,-1,-1):
            out[n] *= post
            post *= nums[n]
        return out