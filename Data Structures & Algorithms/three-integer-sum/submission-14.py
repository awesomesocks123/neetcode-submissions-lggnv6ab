class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        seen = set() 
        """
        nums.sort() [-1,0,1,2,-1,-4]
        nums = [-4,-1,-1,0,1,2]
                 |. |.       |. 
                 i  l.       r. 
        """
        for i in range(n):
            l, r = i + 1, n - 1 # our window 

            while l < r:
                s = nums[i] + nums[l] + nums[r] 

                if s > 0: # reverse logic of the bottom one 
                          # we cycle until we get a number small enough to satisfy 
                    r -= 1
                elif s < 0: # since its sorted 
                            #  -4 + -1 + 2 
                            #  -5 + 2 
                            #  - 3
                            # we want a number that can make this sum to be equal to 3 
                            # so we keep moving left up since its sorted it will give us 
                            # a bigger number 
                    l += 1
                elif s == 0:
                    triplet = tuple([nums[i],nums[l], nums[r]])
                    if triplet not in seen:  
                        seen.add(triplet)
                    l += 1
                    r -= 1
        
        return list(seen) 

