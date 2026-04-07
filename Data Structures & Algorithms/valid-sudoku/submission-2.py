class Solution:
    def isValidSudoku(self, grid: List[List[str]]) -> bool:
        # we must check all columns
        for c in range(9):
            sub_box = set()
            for r in range(9):
                number = grid[r][c]
                if number.isdigit():
                    print(number)
                    number = int(number)
                    if number < 1 or number > 9:
                        return False
                    if number in sub_box:
                        return False
                sub_box.add(number)

        # we must check all rows
        for r in range(9):
            sub_box = set()
            for c in range(9):
                number = grid[r][c]
                if number.isdigit():
                    print(number)
                    number = int(number)
                    if number < 1 or number > 9:
                        return False
                    if number in sub_box:
                        return False
                sub_box.add(number)


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