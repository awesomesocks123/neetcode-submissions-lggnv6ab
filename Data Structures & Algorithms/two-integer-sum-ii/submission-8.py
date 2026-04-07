class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left,right = 0, len(numbers) - 1

        while left < right:
            res = numbers[left] + numbers[right]
            if target == res:
                return[left +1, right+1]
            if res < target:
                left += 1
            else:
                right -= 1
                


