class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for e in s:
            if e.isalnum():
                string += e.lower()
        left,right = 0, len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True