class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #check open < n append open
        #check if close < open we append close
        # if both are counts == n our job is complete we add to our res
        stack = []
        res = []
        def backtrack(openCount, closeCount):
            if openCount == closeCount == n:
                res.append(''.join(stack))
            if openCount < n:
                stack.append('(')
                backtrack(openCount + 1, closeCount)
                stack.pop()
            if closeCount < openCount:
                stack.append(')')
                backtrack(openCount, closeCount + 1)
                stack.pop()
        backtrack(0,0)
        return res


 