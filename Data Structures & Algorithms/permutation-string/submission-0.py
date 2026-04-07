class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = [0] * 26
        window = [0] * 26
        l = 0 
        for c in s1:
            count_s1[ord(c) - ord('a')] += 1

        for r in range(len(s2)):
            window[ord(s2[r]) - ord('a')] += 1
            if (r - l + 1) == len(s1):
                if window == count_s1:
                    return True
                window[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
        return False 

