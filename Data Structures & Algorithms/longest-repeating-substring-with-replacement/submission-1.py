class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        s = "XYYX" , k = 2
        output = 4

        "X XX X"
        "Y YY Y"

        "AAABABB"
        "AAA A ABB" = 5 because 5 a's 


        count of the highest occurent unique letters
        and we just flip what'evers thats not and we use that as our longest


        X YY X Z Y 
        Y YY Y = 4
        Y YY X Y Y = 4

        to keep count we can use a dictionary to keep count 

        how to keep track of counts 

        count dictionary
        key : value
        uppercase enlgish chars : count 


        # how to find our length 
        lenght of the longest
        max_length = 0
        max_length = max(max_length, length of the window + 1)



        #how do we traverse
        #and what condition udo we use to break the loop and fix our windwos


        """

        count = {}
        max_length = 0 

        max_freq = 0 
        l = 0 
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            max_freq = max(max_freq, count[s[r]])

            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)

        return max_length






