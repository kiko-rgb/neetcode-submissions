class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        for row in range(rows):
            row_check = {}
            for col in range(cols):
                if board[row][col] in row_check:
                    return False
                if board[row][col].isnumeric():
                    row_check[board[row][col]] = 1

        for col in range(cols):
            col_check = {}
            for row in range(rows):
                if board[row][col] in col_check:
                    return False
                if board[row][col].isnumeric():
                    col_check[board[row][col]] = 1

        for square in range(9):
            # define the 3 x 3 square:
            square_check = {}
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] in square_check:
                        return False
                    if board[row][col].isnumeric():
                        square_check[board[row][col]] = 1

        return True