class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1, index2 = 0, len(numbers) - 1

        while index1 < index2:
            twosum = numbers[index1] + numbers[index2]
            if twosum == target and index1 != index2:
                return [index1 + 1,index2 + 1]
            
            if twosum > target:
                index2 -= 1
            if twosum < target:
                index1 += 1
