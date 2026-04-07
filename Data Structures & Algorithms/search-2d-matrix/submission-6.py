class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, h = 0 , (len(matrix) * len(matrix[0])) - 1

        while l <= h:
            mid = (l + h) // 2
            r = mid // len(matrix[0])
            c = mid % len(matrix[0])
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                l = mid + 1
            elif matrix[r][c] > target:
                h = mid - 1
        return False

            