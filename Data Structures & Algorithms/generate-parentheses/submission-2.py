class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [("", n, n)]  # (current_string, open_left, close_left)
        result = []
        while stack:
            current, open_left, close_left = stack.pop()

            # If we've used all open and close parentheses, add to result
            if open_left == 0 and close_left == 0:
                result.append(current)
                continue

            # If we can still add an open parenthesis, push a new state
            if open_left > 0:
                stack.append((current + "(", open_left - 1, close_left))

            # If we can add a closing parenthesis, push a new state
            if close_left > open_left:
                stack.append((current + ")", open_left, close_left - 1))

        return result
 