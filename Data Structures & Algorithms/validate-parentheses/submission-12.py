class Solution:
    def isValid(self, s: str) -> bool:

        # we can use a stack for all open paren
        # once we run into close we pop from our stack 
        # then we compare 

        #if our stack is empty once we get to the end of our array its valid 
        #if not we exit returning false


        #we can use dictionary for '[': ']' that way we can keep track of what needs to be returned

        groupings = { ')':'(', ']':'[', '}':'{'}

        stack = [] 

        for c in s:
            if c in groupings:
                if stack and stack[-1] == groupings[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False 
