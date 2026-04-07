class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)

        half = total // 2

        #we have to run binary search on the smaller array
        if len(B) < len(A):
          A,B = B, A

        l, r = 0 , len(A) 
        #we're guaranteed a median so we can just return it when we find it
        #lazy way 
        while l <= r:
          i = (l + r) // 2 #A
          j = half - i  #index of the mid point B

          #any of these could be out of bounds 
          #these bounds are for edge cases 
          Aleft = A[i - 1] if i > 0 else float("-infinity")
          # R_A: A[i] (Min of Right A)
          Aright = A[i] if i < len(A) else float("infinity")
          
          # L_B: B[j-1] (Max of Left B)
          Bleft = B[j - 1] if j > 0 else float("-infinity")
          # R_B: B[j] (Min of Right B)
          Bright = B[j] if j < len(B) else float("infinity")
          
          #partition is correct
          if Aleft <= Bright and Bleft <= Aright:
            #odd 
            if total % 2:
              return min(Aright, Bright)
            #even
            else:
              return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
          
          elif Aleft > Bright:
            r = i - 1
          else:
            l = i + 1