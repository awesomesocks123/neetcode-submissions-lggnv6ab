class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for n, item in enumerate(nums):
            #skip over duplicate
            if n > 0 and item == nums[n-1]:
                continue 
            # set pointer to be end of array
            # and current item +1 index
            l, r = n + 1, len(nums) -1
            while l < r:
                #our currsum if we're doing two sum II
                threesome = item + nums[l] + nums[r] 
                if threesome > 0:
                    r -= 1
                    #this is if our sum is greater than 0 
                    # that means right pointer is too big so we decrement right pointer -1
                elif threesome < 0:
                    l += 1 
                    # this means our left pointer is too small so we need a bigger number
                    # we increment it
                else:
                    res.append([item,nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l +=1

        return res