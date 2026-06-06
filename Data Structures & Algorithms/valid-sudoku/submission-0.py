class Solution:
    def checkSubBoard(self, board, offset_row, offset_col):
        items = []
        for row in range(offset_row, offset_row+3):
            for col in range(offset_col, offset_col+3):
                cell = board[row][col]
                if cell in items:
                    return False
                elif cell == ".":
                    continue
                else:
                    items.append(cell)
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            items = []
            for cell in row:
                if cell in items:
                    return False
                elif cell == ".":
                    continue
                else:
                    items.append(cell)
        for col in range(0, 9):
            items = [] 
            for row in range(0, 9):
                cell = board[row][col]
                if cell in items:
                    return False
                elif cell == ".":
                    continue
                else:
                    items.append(cell)
            

        for offset_row in range(0, 9, 3):
            for offset_col in range(0, 9, 3):
                if not self.checkSubBoard(board, offset_row, offset_col):
                    return False

        return True

            
        