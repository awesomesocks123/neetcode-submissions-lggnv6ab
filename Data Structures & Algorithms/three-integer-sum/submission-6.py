class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        n = len(nums)
        i = 0
        while i < n - 2:
            # skip duplicate anchors, but ADVANCE i
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            if nums[i] > 0:
                break

            j, k = i + 1, n - 1
            target = -nums[i]
            while j < k:
                current_sum = nums[j] + nums[k]

                if current_sum == target:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]: # The issue is here.
                        k -= 1
                elif current_sum < target:
                        j += 1

                else: # current_sum > target
                        k -= 1
            i += 1
        return res




