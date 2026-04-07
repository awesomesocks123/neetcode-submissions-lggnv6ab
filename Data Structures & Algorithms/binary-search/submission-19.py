class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)

        print(len(nums))
        while left < right:
            mid = left + (right - left) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left += 1
            else:
                right -= 1

        return -1