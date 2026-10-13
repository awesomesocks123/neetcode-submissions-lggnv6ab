class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        nums.sort() 
        for i in range(n):
            l,r = i + 1, n - 1 

            while l < r :
                threeSum = nums[i] + nums[l] + nums[r] 

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                elif threeSum == 0:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                    r -= 1
        return [list(t) for t in res]