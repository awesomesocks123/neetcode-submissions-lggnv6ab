'''
Input: board = 
[  c1 ,c2 ,c3 ,c4 ,c5 ,c6 ,c7 ,c8 ,c9 ,
 ["1","2",".",".","3",".",".",".","."]r1,
 ["4",".",".","5",".",".",".",".","."]r2,
 [".","9","8",".",".",".",".",".","3"]r3,
 ["5",".",".",".","6",".",".",".","4"]r4,
 [".",".",".","8",".","3",".",".","5"]r5,
 ["7",".",".",".","2",".",".",".","6"]r6,
 [".",".",".",".",".",".","2",".","."]r7,
 [".",".",".","4","1","9",".",".","8"]r8,
 [".",".",".",".","8",".",".","7","9"]r9]

Output: true
to check subbox 1 
we need to visit 
[c1,r1] ; [c2,r1] ; [c3,r1]
[c1,r2] ; [c2,r2] ; [c3,r2]
[c1,r3] ; [c2,r3] ; [c3,r3]

'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            rowSet = set()
            colSet = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in rowSet:
                    return False
                rowSet.add(board[i][j])
                if board[j][i] !="." and board[j][i] in colSet:
                    return False 
                colSet.add(board[j][i])
                
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subSet = set()
                for r in range(3):
                    for c in range(3):
                        if board[i+r][j+c] != "." and board[i+r][j+c] in subSet:
                            return False
                        subSet.add(board[i+r][j+c])
                        
        return True
        