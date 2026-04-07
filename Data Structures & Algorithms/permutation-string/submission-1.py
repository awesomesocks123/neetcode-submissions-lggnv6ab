class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        left, right = 0,0 
        s1_count = [0] * 26
        #set up count map for s1  we need this s1_count map to compare to our substring map 
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - 97 ] += 1


        substring_count = [0] * 26 
        for right in range(len(s2)):
            # now we must add whatever in our window to the count map
            substring_count[ord(s2[right]) - 97 ] += 1
            while right - left + 1  > len(s1):
                #we're shrinking our window so we can have the correclty sized window to compute
                # does susbtring_count = s1_count
                substring_count[ord(s2[left])-97] -= 1
                #it just decrease number to 0 not remove it from dict we should pop it from dict 
                left += 1
            # now we check if they're equal

            if substring_count == s1_count:
                return True
        return False