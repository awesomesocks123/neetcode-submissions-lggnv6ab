class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { "]" : "[", ")": "(", "}":"{" } 
        stack = []

        for c in s:
            if c not in hashmap:
                stack.append(c)
            else: # if c is in hashmap essentially
                if len(stack) == 0: #if its empty here then theres no pairing 
                # because the stack suppose to have the pairings for the current C
                    return False
                else: #if the stack still has pairings 
                    pairing = stack.pop()
                    if pairing != hashmap[c]: #we check if hte pairings maatches
                        return False #if it doesn't it fails out 
        # we made it to the end of list that is S our given
        #if the stack is 0 and we're able to make it to the end
        #that means all of our bracket pairings are matched and therefore 
        #the stack is 0 
        return len(stack) == 0