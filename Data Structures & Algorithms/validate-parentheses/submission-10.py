class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { "]" : "[", ")": "(", "}":"{" } 
        stack = []

        for c in s:
            if c not in hashmap:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    pairing = stack.pop()
                    if pairing != hashmap[c]:
                        return False
        return len(stack) == 0