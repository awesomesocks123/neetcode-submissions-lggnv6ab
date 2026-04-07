class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }

        tempSum = []
        result = 0 
        for var in tokens:
            if var in operators:
                y = tempSum.pop()
                x  = tempSum.pop()
                result = operators[var](x,y)
                tempSum.append(result)

            else:
                tempSum.append(int(var))

        return tempSum[0] 