class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for e in s:
            if e.isalnum():
                string += e.lower()
        return string == string[::-1]