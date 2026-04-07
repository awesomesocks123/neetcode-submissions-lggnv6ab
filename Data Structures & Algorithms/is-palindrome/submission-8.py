class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for e in s:
            if e.isalnum():
                string += e.lower()
        firsthalf = string[:len(string)//2]
        secondhalf = string[len(string)//2 + len(string) % 2:][::-1]
        return firsthalf == secondhalf