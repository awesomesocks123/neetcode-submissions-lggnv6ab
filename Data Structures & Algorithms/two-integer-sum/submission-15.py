class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        numDict = {}
        index = 0 
        for e in nums: 
            diff = target - e
            if diff in numDict:
                return [numDict[diff], index]
            numDict[e] = index
            index += 1
            
            