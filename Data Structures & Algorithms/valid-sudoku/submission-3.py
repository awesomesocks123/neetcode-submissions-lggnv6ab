class Solution:
    def isValidSudoku(self, grid: List[List[str]]) -> bool:
        # we must check all columns
        cols_set = [set() for _ in range(9)]
        rows_set = [set() for _ in range(9)]

        # we must check all rows
        for r in range(9):
            for c in range(9):
                number = grid[r][c]
                if number != '.':
                    if number in cols_set[c] or number in rows_set[r]:
                        return False
                cols_set[c].add(number)
                rows_set[r].add(number)


        # we must check all sub boxes 
        for box_row in range(0, 9, 3):      # 0, 3, 6
            for box_col in range(0, 9, 3):  # 0, 3, 6
        # Print one 3x3 box
                sub_box = set() 
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        number = grid[r][c]
                        if number.isdigit():
                            print(number)
                            number = int(number)
                            if number < 1 or number > 9:
                                return False
                            if number in sub_box:
                                return False
                        sub_box.add(number)
        return True 