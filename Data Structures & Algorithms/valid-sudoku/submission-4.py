class Solution:
    def isValidSudoku(self, grid: List[List[str]]) -> bool:
        # we must check all columns
        cols_set = [set() for _ in range(9)]
        rows_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]

        # we must check all rows
        for r in range(9):
            for c in range(9):
                number = grid[r][c]
                box_idx = (r // 3) * 3 + (c // 3)
                if number != '.':
                    if number in cols_set[c] or number in rows_set[r] or number in box_set[box_idx]:
                        return False
                cols_set[c].add(number)
                rows_set[r].add(number)
                box_set[box_idx].add(number) 

        return True 