class Solution:
    def trap(self, height: List[int]) -> int:
        """
        given an array of non negative integers

        height[i] represente height of a bar with width of 1

        return maximum area of water that can be trapped between bars. 

        we take our left and right and current height[i] 

        we first calculate the possible area we can have which is min(left, right) heights then we subtract height[i] to see 
        how much water we can actually store 

        we can use a prefix and suffix array?

        leftMax -> i and i-1? 
        - where we can keep track max(current, LeftMax)
        --> as we iterate thru we build it out compairing i and i-1 
        ---> so with given [0,2,0,3,1,0,1,3,2,1]
        -----> leftmax array would look like [0,2,2,3,3,3,3,3,3,3]
        ------> rightmax woudl look like [3,3,3,3,3,3,3,2,1,1]
        now we can just compute min(leftmax[i], rightmax[i]) - height[i]
        and += the answer 

        and we should get the result 

        
        rightMax  <- j and j+1? 
        """
        
        leftmax = [0] * len(height)
        rightmax = [0] * len(height) 
        n = len(height)
        if n == 0:
            return 0
        leftmax[0] = height[0] 
        for i in range(1, len(height)):
            leftmax[i] = max(leftmax[i-1], height[i])

        rightmax[len(height)-1] = height[len(height) - 1]

        for i in range(len(height)-2, -1,-1):
            rightmax[i] = max(rightmax[i+1], height[i])
        print(leftmax)
        print(rightmax)
        res = 0 
        for i in range(len(height)):
            res += min(leftmax[i], rightmax[i]) - height[i]
        return res 
        