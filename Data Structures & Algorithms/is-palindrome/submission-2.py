class Solution:
    def isPalindrome(self, s: str) -> bool:
        z = []
        for i in s:
            if i.isalnum():
                z.append(i.lower())
        j = z.copy()
        j.reverse()

        for n in range(len(z)):
            if z[n] != j[n]:
                return False
        return True
