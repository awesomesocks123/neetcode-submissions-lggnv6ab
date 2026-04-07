class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # #naive solution 
        # # we have a start and end

        # # start is first letter
        # # then we add this letter to a set
        # # then we move to next character and add this to our set
        # # if we enctoure the same leetter in our set
        # # we just return the size of the set

        # letters = set()
        # max_letters = 0 
        # for i in range(len(s)):
        #     if s[i] in letters:
        #         max_letters = max(max_letters,len(letters))
        #         letters.clear()
        #     letters.add(s[i])
        
        # return max_letters 
        # #     pww we shouldnt' return 
        # #     we must keep going
        # #     so we need to reset 
        # #     kew 
        # # we keep going if we have repeateings we should reset our set insetaed and do this 

        # we can use a dictionary to keep track of positions
        #update positions as we go on 

        if not s:
            return 0 
        #we must make a dictionary that keep tracks of unique characters
        #if we encounter a char that is in our dictionary
        #we update that char with a new index
        # but how do we update our left pointer?
        # zxyzxyz
        # ||
        # | |
        #  ||| 
        #we just move left up 1 or to our right? 
        #well we know everything in between left and right is unique so if a repeat comes up we should just make our left equal to our right
        # but what if we have something like this zxyzjki wouldnt longest unique be 
        # xyzjki?
        # if we move left to our right we would get 
        # zjki not coutning the y
        # so we should only slide the window so that there are no duplicates in sisde the window making it left += 1
        #we also add new chars and their index into the dicitonary
        #char as key and value is the index 
        #zxyzzzzzz
        unique = {} 
        maxcounter = 0
        left, right = 0,0
        while right < len(s):
            if s[right] in unique:
                left = max(unique[s[right]] +1, left)
            unique[s[right]] = right 
            count = right - left + 1
            maxcounter = max(count,maxcounter)
            #add to our dictionary
            right += 1
        return maxcounter
            










