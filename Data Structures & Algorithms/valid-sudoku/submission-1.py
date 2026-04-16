class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_boxes = [[set() for _ in range(3)] for _ in range(3)]
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                
                num = int(board[row][col])

                if num in sub_boxes[row//3][col//3]:
                    print(f'sub-box: {row, col}')
                    print(f'sub-box {row//3, col//3}: {sub_boxes[row//3][col//3]}')
                    return False

                sub_boxes[row//3][col//3].add(num)
                
                if num in row_sets[row]:
                    print(f'row: {row, col}')
                    return False
                
                row_sets[row].add(num)

                if num in col_sets[col]:
                    print(f'col: {row, col}')
                    return False

                col_sets[col].add(num)

        return True