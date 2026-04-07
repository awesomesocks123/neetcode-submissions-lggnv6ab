class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ''
        for string in strs:
            encode += str(len(string)) + '#' + string
        return encode 

    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0 
        # get the first number
        # find the #

        # count until we reach the next number 

        #add the length of the string to our arrays

        while i < len(s):
            j = i 
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            i = j + 1
            j = length + i 
            decode.append(s[i:j])

            i = j 
        return decode 
