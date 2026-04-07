class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decode = []
        start = 0
        while start < len(s):
            end = start 
            while s[end] != '#':
                end += 1
            # now we get into position to move 
            length = int(s[start:end])
            # we get our length so we know how long the word is 
            start = end + 1 # we move it passed '#' so we can get to the true start
            end = start + length # our true ending
            decode.append(s[start:end])
            #move our start pointer
            start = end 
        return decode


            

