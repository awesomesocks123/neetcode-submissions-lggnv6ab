class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        given an array of integers temperatures where temp[i] is the daily temp on ith day

        return the array result where result[i] is the number of days after the ith day
        before a warmer temperature appears on a future day

        if there is no day in the future where a warmer temp will appear for the ith day
        - set result[i] = 0 

        
        example 1: temperatures = [30,38,30,36,35,40,28]
        output = [1,4,1,2,1,0,0]
                 [1,4,1,2,1,0,0]
        30 -> 38
        1 because the next day the temp is higher than current
        38 -> 40 
        4 because 38 > 30, 38 > 36, 38 > 35, 38 !> 40
        30 -> 36
        1 30 !> 36
        36 -> 40
        2 36 > 35, 36 !> 40
        35 -> 40
        1 35 !> 40
        40 -> end of list 
        0 cuz nothing is greater than 40
        28 
        0 cuz nothing is greater than 40

        1,4,1,1,2,1,0,0

        we can use nested loop for the naive solution however it will be inneficiant and will be
        o(n^2)
        basically 
        i -> until theres a greater if theres greater record the j count j - i
        and keep going for all of i and j 


        what can we use thats better?
        - use a stack?
        - we push current temp[i]
        then we can compare if the next element is greater if it is we can pop it and return the length? 
        
        """

        res = [0] * len(temperatures)

        stack = []


        for i, temp in enumerate(temperatures):
            #critical checker here 
            while stack and temperatures[stack[-1]] < temp:

                pop = stack.pop()

                res[pop] = i - pop

            stack.append(i)

        return res
                













