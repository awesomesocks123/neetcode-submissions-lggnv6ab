class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        complement = {'(' : ')', '{': '}', '[':']'}

        for c in s:
            if c in complement:
                stack.append(c)
            elif len(stack) == 0 or complement[stack.pop()] != c:
                return False
        return len(stack) == 0