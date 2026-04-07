from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)  # Truncate toward zero
        }

        stack = []

        for token in tokens:
            if token in operators:
                y = stack.pop()
                x = stack.pop()
                result = operators[token](x, y)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]
