class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot: # searching for the row in which the solution is
            row = (top + bot) // 2
            print("Searching row in which the solution is: ", row)
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        print("top, bot: ", top, bot)
        
        if not (top <= bot): # checking if pointers have crossed
            return False

        row = (top + bot) // 2
        print("row: ", row)

        l, r = 0, COLS - 1
        print(" --- Entering line search --- ")
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

        