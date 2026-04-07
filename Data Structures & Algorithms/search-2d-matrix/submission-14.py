class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """

        standard binary search instead of 1d its 2d 
        do we nest the bin search?

        we just need to know if the max of each subarray exist or actually just use [i][j] 

        just have to flatten out this matrix

        matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
        0,0 0,1 0,2 0,3   1,0 1,1 1,2, 1,3.   2,0 2,1, 2,2 2,3
        theres 12 here 

        12 / 2 = 6

        6 / 3 = 2
        6/3 6/4 

        Row index: row = mid // number_of_columns
        Column index: column = mid % number_of_column




        
        
        """
        m = len(matrix[0]) #col
        n = len(matrix) #row

        left = 0
        right = m * n - 1 #compute m x n

        while left <= right:
            mid = left + (right - left) // 2

            row = mid // m
            col = mid % m
            #now we do a check
            if matrix[row][col] < target:
                left = mid + 1
            elif matrix[row][col] > target:
                right = mid - 1
            elif matrix[row][col] == target:
                return True
            
        return False




