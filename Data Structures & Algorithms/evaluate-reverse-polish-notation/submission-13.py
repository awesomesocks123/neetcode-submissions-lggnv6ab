class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #init stack
        stack = []
        for token in tokens:
            if token == '+':
                #doesn't matter order add
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                #order matters
                x, y = stack.pop(),stack.pop()
                stack.append(y - x)
            elif token == '*':
                #order doesn' tmatter 
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                #order matters x y / -> y / x  
                x, y = stack.pop(),stack.pop()
                stack.append(int(float(y) / x))
            else:
                stack.append(int(token))
        return stack[0] 