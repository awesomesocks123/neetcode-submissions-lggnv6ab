class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return "" 

        

        count_T, window = {}, {}
        res, resLen = [-1,-1], float("infinity") 
        left = 0 


        #initiate our T Count 
        for char in t:
            count_T[char] = count_T.get(char, 0) + 1

        have, need = 0 , len(count_T) 
        print(len(t))
        print(len(count_T))
        for right in range(len(s)):
            char = s[right] 
            window[char] = window.get(char,0) + 1 

            if char in count_T and count_T[char] == window[char]:
                have += 1 
            
            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                window[s[left]] -= 1 
                
                if s[left] in count_T and window[s[left]] < count_T[s[left]]: 
                    have -= 1 
                left += 1
        
        left, right = res

        return s[left:right + 1] if resLen != float("infinity") else "" 