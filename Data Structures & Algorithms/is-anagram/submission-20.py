class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram have same letter count 
        # the brute force solution 
        """
            nested loop to on S and check if T has it and also check if hte count of
            either S[i] and T[i] are equal in count 

            o(n^2) 

            potential bugs and edge cases ? 
                - how do we dicern if current S[i] is different from S[i+1] 
                    like if word letter vs rettel how do we know 
                                    |.        | these T are already accounted for?
                - or we check motorsport vs sportmotor 
        
        
        """

        """
        intuitive solution:
            we must keep count of each unique letter
            once we come across this letter when doing S[i] vs T[i] we must decrease the count
            or keep track of a way to know the letter has been accounted for 
            i.e. speed vs spear 


            we can use dictionary as a freqmap

            - we can also init fixed array since alphabet has only 26 letters we can do 
            [0] * 26 

            and so that way 
            each postiion like freq_array[0] = a and freq_array[25] = z 

            and well just update i+=1 so that way freq_array[0] = count 
            and we know its a because we use the index to identify 

        """

        freq_array = [0] * 26 

        # now we it thru each S[i] and T[i] and increment / decremtn as we go 

        # we can check it wont be an anagram if the len are differnet
        if len(s) != len(t):
            return False 

        n = len(s)  # easier to keep track 

        for i in range(n):
            # must get the letter
            char = s[i] # now we must make into number between 0-25 
            char = char.lower() 
            freq_array[ord(char) - ord('a')] += 1 
        
            # now we build the freqmap 

            #at the sametime we can prep to decrement t by doing 

            T_char = t[i].lower() 

            freq_array[ord(T_char) - ord('a')] -= 1

        # we just return for all if freq array if everythign is at 0 we should be green 

        return all(count == 0 for count in freq_array)      




        










